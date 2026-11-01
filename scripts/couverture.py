#!/usr/bin/env python3
"""Mesure la couverture des racines de scripts/racines.json et propose celles qui manquent.

Classe un échantillon d'articles : les plus lus (tête) et un tirage au hasard dans le
reste du classement (longue traîne, qui fera l'essentiel du pool de cartes). Écrit un
rapport en Markdown avec :

  1. la répartition par type, exclus et sans type, pour chaque groupe
  2. les classes Wikidata directes des articles SANS type, par nombre d'articles
  3. des racines candidates : les classes ancêtres qui règlent le plus d'articles sans
     type (couverture gloutonne), en écartant les classes trop générales
  4. les articles classés par une racine très générale (concept, objet artificiel,
     occurrence...), dont le type est le plus douteux

On choisit ensuite, pour chaque ligne qui vaut la peine, un type ou « exclu », et on
l'ajoute dans scripts/racines.json. On relance pour voir la couverture monter.

Usage :
  python3 scripts/couverture.py --classement .dumps/fr-2026-10.tsv \\
      --tete 1500 --hasard 1500 --sortie .dumps/couverture-fr.md
"""

import argparse
import collections
import json
import os
import random
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tirer_echantillon as t  # noqa: E402

# Racines assez générales pour que le type qu'elles donnent soit à vérifier.
GENERIQUES = {"Q151885", "Q8205328", "Q1190554", "Q43229", "Q2221906", "Q11016"}
# Une classe ancêtre de plus de cette part des articles classés est trop générale
# pour devenir une racine (« entité », « objet »...).
SEUIL_GENERALITE = 0.04


def lire_echantillon(chemin, tete, hasard, graine):
    """-> liste de (groupe, lectures, qid, titre)"""
    lignes = []
    with open(chemin, encoding="utf-8") as f:
        total = sum(1 for _ in f)
    rng = random.Random(graine)
    tires = set(rng.sample(range(tete, total), min(hasard, total - tete)))
    with open(chemin, encoding="utf-8") as f:
        for i, ligne in enumerate(f):
            if i < tete:
                groupe = "tête"
            elif i in tires:
                groupe = "hasard"
            else:
                continue
            n, qid, titre = ligne.rstrip("\n").split("\t", 2)
            if not titre.startswith(t.PREFIXES_LISTES):
                lignes.append((groupe, int(n), qid, titre))
    return lignes


def libelles(ids, contact):
    res = {}
    ids = sorted(ids)
    for i in range(0, len(ids), 50):
        lot = ids[i:i + 50]
        rep = t.http_json(t.API_WIKIDATA, params={
            "action": "wbgetentities", "format": "json", "props": "labels",
            "languages": "fr|en", "ids": "|".join(lot),
        }, contact=contact)
        for q, e in (rep or {}).get("entities", {}).items():
            lab = e.get("labels", {})
            res[q] = (lab.get("fr") or lab.get("en") or {}).get("value", q)
    return res


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--classement", required=True)
    p.add_argument("--tete", type=int, default=1500, help="articles les plus lus")
    p.add_argument("--hasard", type=int, default=1500, help="articles tirés au hasard dans le reste")
    p.add_argument("--graine", type=int, default=1)
    p.add_argument("--top", type=int, default=40, help="lignes par tableau")
    p.add_argument("--sortie", required=True)
    p.add_argument("--contact", default=t.CONTACT)
    a = p.parse_args()

    articles = lire_echantillon(a.classement, a.tete, a.hasard, a.graine)
    print(f"{len(articles)} articles à classer...", file=sys.stderr)

    info = {}  # qid -> dict
    for i in range(0, len(articles), t.TAILLE_LOT):
        lot = articles[i:i + t.TAILLE_LOT]
        types, p31, anc = t.classer_lot([q for _, _, q, _ in lot], a.contact)
        for groupe, n, q, titre in lot:
            info[q] = {"groupe": groupe, "titre": titre, "type": types[q], "p31": p31[q],
                       "anc": anc[q], "racine": t.RACINE_TROUVEE.get(q)}
        print(f"  {min(i + t.TAILLE_LOT, len(articles))} classés", file=sys.stderr)

    classes = [v for v in info.values()]
    sans_type = {q: v for q, v in info.items() if v["type"] is None}
    classes_ok = [v for v in info.values() if v["type"] in t.TYPES]

    # classes trop générales : ancêtres d'une grande part des articles classés
    freq = collections.Counter(c for v in classes_ok for c in v["anc"])
    trop_generales = {c for c, n in freq.items() if n > SEUIL_GENERALITE * max(1, len(classes_ok))}

    # couverture gloutonne
    restants = set(sans_type)
    suggestions = []
    while restants and len(suggestions) < a.top:
        compte = collections.Counter()
        for q in restants:
            for c in sans_type[q]["anc"]:
                if c not in trop_generales:
                    compte[c] += 1
        if not compte:
            break
        c, n = max(compte.items(), key=lambda x: (x[1], x[0]))
        couverts = {q for q in restants if c in sans_type[q]["anc"]}
        suggestions.append((c, n, sorted(couverts)[:3]))
        restants -= couverts

    directes = collections.Counter(c for v in sans_type.values() for c in v["p31"])
    generiques = collections.Counter()
    exemples_gen = {}
    for q, v in info.items():
        if v["racine"] in GENERIQUES and v["type"] in t.TYPES:
            for c in v["p31"]:
                generiques[(v["racine"], c)] += 1
                exemples_gen.setdefault((v["racine"], c), v["titre"])

    a_nommer = set(directes) | {c for c, _, _ in suggestions} | {c for r, c in generiques} | GENERIQUES
    nom = libelles(a_nommer, a.contact)

    def exemples(classe, source):
        return ", ".join([v["titre"] for v in source.values() if classe in v["p31"]][:3])

    out = ["# Couverture des racines Wikidata", "",
           f"Échantillon : {a.tete} articles les plus lus + {a.hasard} au hasard dans le reste "
           f"(graine {a.graine}).", "", "## Répartition", "",
           "| Groupe | " + " | ".join(t.TYPES) + " | exclu | sans type | total |",
           "|---|" + "---|" * (len(t.TYPES) + 3)]
    for g in ("tête", "hasard"):
        vs = [v for v in info.values() if v["groupe"] == g]
        c = collections.Counter(v["type"] for v in vs)
        sans = c.get(None, 0)
        out.append(f"| {g} | " + " | ".join(str(c.get(ty, 0)) for ty in t.TYPES)
                   + f" | {c.get('exclu', 0)} | {sans} ({100 * sans // max(1, len(vs))} %) | {len(vs)} |")

    out += ["", "## Classes directes des articles sans type", "",
            "| Articles | Classe | Libellé | Exemples |", "|---|---|---|---|"]
    for c, n in directes.most_common(a.top):
        out.append(f"| {n} | {c} | {nom.get(c, c)} | {exemples(c, sans_type)} |")

    out += ["", "## Racines candidates (couverture gloutonne)", "",
            "Chaque ligne règle des articles sans type en ajoutant cette classe comme racine ou exclusion.", "",
            "| Articles réglés | Classe | Libellé | Exemples |", "|---|---|---|---|"]
    for c, n, ex in suggestions:
        out.append(f"| {n} | {c} | {nom.get(c, c)} | {', '.join(sans_type[q]['titre'] for q in ex)} |")
    out.append(f"\nIl resterait {len(restants)} articles sans type après ces {len(suggestions)} ajouts.")

    out += ["", "## Classés par une racine très générale (à vérifier)", "",
            "| Articles | Racine | Classe directe | Libellé | Exemple |", "|---|---|---|---|---|"]
    for (r, c), n in generiques.most_common(a.top):
        out.append(f"| {n} | {nom.get(r, r)} | {c} | {nom.get(c, c)} | {exemples_gen[(r, c)]} |")

    with open(a.sortie, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print(f"Rapport écrit dans {a.sortie}", file=sys.stderr)


if __name__ == "__main__":
    main()
