#!/usr/bin/env python3
"""Tire un échantillon d'articles Wikipédia, des plus lus aux moins lus.

Voir docs/generation/echantillon.md pour le format de sortie (JSON Lines).

Entrée : le classement produit par scripts/preparer_dumps.py (tous les articles du
wiki triés par lectures du mois, avec leur QID Wikidata).

Étapes, en parcourant le classement du plus lu au moins lu, par lots de 50 :
  1. Wikidata (API wbgetentities) : classes P31 de chaque article.
  2. Wikidata (API wbgetentities) : classes parentes (P279), gardées en mémoire.
  3. Exclusions : l'article est écarté si une de ses classes ancêtres est exclue.
  4. Type de carte = racine la plus proche des classes P31 (liens P279).
  5. REST summary : résumé des articles gardés.

On s'arrête quand chaque type a --par-type articles, ou après --max-examines
articles examinés. Les articles sans type sont ignorés. Les réponses des API sont
gardées dans .cache-echantillon/.

Usage :
  python3 scripts/tirer_echantillon.py --classement .dumps/fr-2026-10.tsv \\
      --langue fr --par-type 10 --sortie echantillon/echantillon-fr.jsonl
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

CONTACT = "https://github.com/Elnop/wikidado"
TYPES = ["creature", "lieu", "evenement", "objet", "savoir", "faction"]

# Classes racines par type de carte et classes exclues : voir scripts/racines.json
# (provisoire, voir gameplay/carte/type.md et generation/article/selection.md).
# Le type d'un article est celui de la racine la plus proche de ses classes P31, en
# comptant les liens "sous-classe de" (P279). À distance égale, l'ordre de TYPES
# départage. scripts/couverture.py aide à trouver les racines qui manquent.
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "racines.json"), encoding="utf-8") as _f:
    _racines = json.load(_f)
RACINES = {t: [r["id"] for r in rs] for t, rs in _racines["types"].items()}
EXCLUSIONS = {r["id"] for r in _racines["exclusions"]}

# "Wikipédia:Accueil" est une page de service ; "Star Wars: Episode I" est un article.
ESPACE_DE_NOM = re.compile(r"^[^_:]+:")
PREFIXES_LISTES = ("Liste de", "Liste des", "Liste d'", "List of")

TAILLE_LOT = 50
PROFONDEUR_MAX = 12
DOSSIER_CACHE = ".cache-echantillon"
utiliser_cache = True
API_WIKIDATA = "https://www.wikidata.org/w/api.php"


def http_json(url, params=None, contact=CONTACT, essais=4):
    if params:
        url = url + "?" + urllib.parse.urlencode(params)
    fichier = None
    if utiliser_cache:
        cle = hashlib.sha1(url.encode()).hexdigest()
        fichier = os.path.join(DOSSIER_CACHE, cle + ".json")
        if os.path.exists(fichier):
            with open(fichier, encoding="utf-8") as f:
                return json.load(f)
    req = urllib.request.Request(url, headers={
        "User-Agent": f"wikidado-echantillon/0.1 ({contact})",
        "Accept": "application/json",
    })
    for essai in range(essais):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                rep = json.load(r)
            if fichier:
                os.makedirs(DOSSIER_CACHE, exist_ok=True)
                with open(fichier, "w", encoding="utf-8") as f:
                    json.dump(rep, f, ensure_ascii=False)
            return rep
        except (urllib.error.URLError, json.JSONDecodeError) as e:
            if isinstance(e, urllib.error.HTTPError) and e.code == 404:
                return None
            if essai == essais - 1:
                raise
            time.sleep(2 ** essai)


TITRES = {}  # (langue, QID) -> titre de l'article, lu dans les liens de site Wikidata


def classes_liees(qids, propriete, contact):
    """QID -> ensemble des QID liés par la propriété (P31 ou P279), par lots de 50.

    Au passage, retient le titre de l'article de chaque langue (liens de site).
    """
    res = {}
    qids = list(qids)
    for i in range(0, len(qids), TAILLE_LOT):
        lot = qids[i:i + TAILLE_LOT]
        rep = http_json(API_WIKIDATA, params={
            "action": "wbgetentities", "format": "json", "props": "claims|sitelinks",
            "ids": "|".join(lot),
        }, contact=contact)
        entites = (rep or {}).get("entities", {})
        for q in lot:
            for cle, lien in entites.get(q, {}).get("sitelinks", {}).items():
                if cle.endswith("wiki") and len(cle) == 6:
                    TITRES[(cle[:2], q)] = lien["title"]
            valeurs = set()
            for decl in entites.get(q, {}).get("claims", {}).get(propriete, []):
                if decl.get("rank") == "deprecated":
                    continue
                valeur = decl.get("mainsnak", {}).get("datavalue", {}).get("value")
                if isinstance(valeur, dict) and "id" in valeur:
                    valeurs.add(valeur["id"])
            res[q] = valeurs
        time.sleep(0.2)
    return res


PARENTS = {}  # classe -> classes parentes (P279), mémoire du processus
RACINE_TROUVEE = {}  # QID -> racine qui a décidé du type (pour scripts/couverture.py)


def classer_lot(qids, contact):
    """-> ({QID: type de carte, "exclu" ou None si sans type}, {QID: P31}, {QID: ancêtres})"""
    racine_type = {r: t for t, rs in RACINES.items() for r in rs}
    ordre = {t: i for i, t in enumerate(TYPES)}
    p31 = classes_liees(qids, "P31", contact)
    type_de = {q: None for q in qids}
    exclu = {q: False for q in qids}
    front = {q: set(p31[q]) for q in qids}
    vus = {q: set(p31[q]) for q in qids}
    for _ in range(PROFONDEUR_MAX + 1):
        for q in qids:
            if front[q] & EXCLUSIONS:
                exclu[q] = True
            if type_de[q] is None:
                trouves = [c for c in front[q] if c in racine_type]
                if trouves:
                    racine = min(trouves, key=lambda c: (ordre[racine_type[c]], c))
                    type_de[q] = racine_type[racine]
                    RACINE_TROUVEE[q] = racine
        actifs = [q for q in qids if front[q] and not exclu[q]]
        if not actifs:
            break
        a_chercher = set().union(*(front[q] for q in actifs)) - PARENTS.keys()
        PARENTS.update(classes_liees(a_chercher, "P279", contact))
        for q in actifs:
            suivants = set().union(*(PARENTS[c] for c in front[q])) - vus[q]
            vus[q] |= suivants
            front[q] = suivants
    return {q: ("exclu" if exclu[q] else type_de[q]) for q in qids}, p31, vus


def resume(langue, titre, contact):
    url = (f"https://{langue}.wikipedia.org/api/rest_v1/page/summary/"
           + urllib.parse.quote(titre.replace(" ", "_"), safe=""))
    try:
        rep = http_json(url, contact=contact)
    except urllib.error.HTTPError:
        return ""
    return (rep or {}).get("extract", "")


def deja_tires(chemins):
    vus = set()
    for c in chemins:
        with open(c, encoding="utf-8") as f:
            for ligne in f:
                if ligne.strip():
                    vus.add(json.loads(ligne)["article"])
    return vus


def lire_classement(chemin):
    """Générateur (lectures, qid, titre), du plus lu au moins lu."""
    with open(chemin, encoding="utf-8") as f:
        for ligne in f:
            n, qid, titre = ligne.rstrip("\n").split("\t", 2)
            yield int(n), qid, titre


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--classement", required=True, help="TSV produit par preparer_dumps.py")
    p.add_argument("--langue", choices=["fr", "en"], required=True)
    p.add_argument("--par-type", type=int, default=10, help="articles à garder par type de carte")
    p.add_argument("--max-examines", type=int, default=50000, help="articles examinés au plus")
    p.add_argument("--exclure", nargs="*", default=[], help="fichiers JSONL dont on ignore les articles")
    p.add_argument("--sortie", required=True)
    p.add_argument("--sans-cache", action="store_true", help="ignore le cache disque (.cache-echantillon/)")
    p.add_argument("--contact", default=CONTACT, help="contact mis dans le User-Agent")
    a = p.parse_args()

    global utiliser_cache
    utiliser_cache = not a.sans_cache
    vus = deja_tires(a.exclure)
    compte = {t: 0 for t in TYPES}
    sortie = []
    examines = 0
    lot = []

    def traiter(lot):
        types, p31, _ = classer_lot([q for _, q, _ in lot], a.contact)
        for n, q, titre in lot:
            t = types[q]
            titre = TITRES.get((a.langue, q))  # titre officiel, celui du dump peut venir d'une redirection
            if (t not in TYPES or q in vus or compte[t] >= a.par_type or titre is None
                    or ESPACE_DE_NOM.match(titre.replace(" ", "_"))
                    or titre.startswith(PREFIXES_LISTES)):
                continue
            compte[t] += 1
            sortie.append({
                "article": q, "langue": a.langue, "titre": titre, "type": t,
                "fiche": {"resume": resume(a.langue, titre, a.contact),
                          "p31": sorted(p31[q]), "lectures": n},
                "attendu": [], "annotateur": None, "difficile": False,
            })
        print(f"  {examines} examinés : {compte}", file=sys.stderr)

    for n, qid, titre in lire_classement(a.classement):
        lot.append((n, qid, titre))
        examines += 1
        if len(lot) == TAILLE_LOT:
            traiter(lot)
            lot = []
            if all(c >= a.par_type for c in compte.values()) or examines >= a.max_examines:
                break
    if lot:
        traiter(lot)

    with open(a.sortie, "w", encoding="utf-8") as f:
        for ligne in sortie:
            f.write(json.dumps(ligne, ensure_ascii=False) + "\n")
    print(f"{len(sortie)} articles écrits dans {a.sortie} : {compte}", file=sys.stderr)
    manquants = [t for t, c in compte.items() if c < a.par_type]
    if manquants:
        print(f"Types incomplets après {examines} articles examinés : {manquants}", file=sys.stderr)


if __name__ == "__main__":
    main()
