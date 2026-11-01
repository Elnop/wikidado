#!/usr/bin/env python3
"""Tire un échantillon d'articles Wikipédia, des plus lus aux moins lus.

Voir docs/generation/echantillon.md pour le format de sortie (JSON Lines).

Étapes :
  1. API Pageviews : top des articles les plus lus du mois (1000 maximum).
  2. API Wikipédia : identifiant Wikidata (QID) de chaque article.
  3. SPARQL Wikidata : type de carte déduit de la classe (P31/P279*), classes exclues écartées.
  4. REST summary : résumé de l'article.

On garde les articles dans l'ordre de lecture, jusqu'à avoir --par-type
articles de chaque type de carte. Les articles sans type reconnu (listes,
œuvres, pages spéciales...) sont ignorés.

Usage :
  python3 scripts/tirer_echantillon.py --langue fr --par-type 10 --sortie echantillon-fr.jsonl
  python3 scripts/tirer_echantillon.py --langue en --exclure echantillon-fr.jsonl ...
"""

import argparse
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date

CONTACT = "https://github.com/Elnop/wikidado"
TYPES = ["creature", "terrain", "evenement", "technique"]

# Classes racines par type de carte. Provisoire : voir gameplay/carte/type.md
# et generation/article/selection.md. L'ordre fixe la priorité si plusieurs
# types conviennent.
RACINES = {
    "creature": ["Q5", "Q16521"],  # être humain, taxon
    "evenement": ["Q1656682", "Q178561", "Q645883"],  # événement, bataille, opération militaire
    "technique": ["Q39546", "Q7397", "Q11862829", "Q11019"],  # outil, logiciel, discipline, machine
    "terrain": ["Q2221906", "Q41176", "Q811979"],  # lieu, bâtiment, structure architecturale
}

TAILLE_LOT = 25  # petits lots : le SPARQL Wikidata coupe les requêtes longues

# Classes exclues pour l'instant (voir generation/article/selection.md) : sites web,
# plateformes, réseaux sociaux (type de carte pas encore décidé) et jeux vidéo (œuvres).
EXCLUSIONS = [
    "Q35127",      # site web
    "Q19967801",   # service en ligne
    "Q118140435",  # très grande plateforme en ligne
    "Q3220391",    # réseau social
    "Q122759350",  # plateforme de contenu généré par les utilisateurs
    "Q6576792",    # communauté en ligne
    "Q4182287",    # moteur de recherche
    "Q33120876",   # projet de contenu Wikimedia
    "Q7889",       # jeu vidéo
]

EXCLUS_PREFIXES = ("Liste_", "List_of_", "Liste_des_")


def http_json(url, params=None, data=None, contact=CONTACT, essais=4):
    if params:
        url = url + "?" + urllib.parse.urlencode(params)
    corps = urllib.parse.urlencode(data).encode() if data else None
    req = urllib.request.Request(url, data=corps, headers={
        "User-Agent": f"wikidado-echantillon/0.1 ({contact})",
        "Accept": "application/json",
    })
    for essai in range(essais):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except (urllib.error.URLError, json.JSONDecodeError) as e:
            if isinstance(e, urllib.error.HTTPError) and e.code == 404:
                return None
            if essai == essais - 1:
                raise
            time.sleep(2 ** essai)


def mois_precedent():
    j = date.today()
    return (j.year, j.month - 1) if j.month > 1 else (j.year - 1, 12)


def top_articles(langue, annee, mois, contact):
    url = (f"https://wikimedia.org/api/rest_v1/metrics/pageviews/top/"
           f"{langue}.wikipedia/all-access/{annee}/{mois:02d}/all-days")
    rep = http_json(url, contact=contact)
    articles = rep["items"][0]["articles"]
    gardes = []
    for a in articles:
        titre = a["article"]
        if ":" in titre or titre.startswith(EXCLUS_PREFIXES):
            continue
        gardes.append({"titre": titre.replace("_", " "), "lectures": a["views"]})
    return gardes


def qids(langue, titres, contact):
    """Titre -> QID, par lots de 50."""
    res = {}
    for i in range(0, len(titres), 50):
        lot = titres[i:i + 50]
        rep = http_json(f"https://{langue}.wikipedia.org/w/api.php", data={
            "action": "query", "format": "json", "redirects": 1,
            "prop": "pageprops", "ppprop": "wikibase_item",
            "titles": "|".join(lot),
        }, contact=contact)
        q = rep.get("query", {})
        renvois = {r["from"]: r["to"] for r in q.get("redirects", [])}
        normal = {n["from"]: n["to"] for n in q.get("normalized", [])}
        par_titre = {p["title"]: p.get("pageprops", {}).get("wikibase_item")
                     for p in q.get("pages", {}).values()}
        for t in lot:
            fin = renvois.get(normal.get(t, t), normal.get(t, t))
            res[t] = par_titre.get(fin)
        time.sleep(0.2)
    return res


def types_wikidata(liste_qids, contact):
    """QID -> (type de carte, liste des P31), via SPARQL."""
    res = {}
    toutes = {r: t for t, rs in RACINES.items() for r in rs}
    racines_v = " ".join(f"wd:{r}" for r in toutes)
    for i in range(0, len(liste_qids), TAILLE_LOT):
        lot = liste_qids[i:i + TAILLE_LOT]
        items = " ".join(f"wd:{q}" for q in lot)
        # Deux requêtes simples : un OPTIONAL autour du chemin P31/P279* est trop lent.
        req_racines = f"""
SELECT ?item ?racine WHERE {{
  VALUES ?item {{ {items} }}
  VALUES ?racine {{ {racines_v} }}
  ?item wdt:P31/wdt:P279* ?racine
}}"""
        req_p31 = f"""
SELECT ?item ?p31 WHERE {{
  VALUES ?item {{ {items} }}
  ?item wdt:P31 ?p31
}}"""
        req_exclus = f"""
SELECT DISTINCT ?item WHERE {{
  VALUES ?item {{ {items} }}
  VALUES ?exclu {{ {" ".join("wd:" + e for e in EXCLUSIONS)} }}
  ?item wdt:P31/wdt:P279* ?exclu
}}"""
        exclus = http_json("https://query.wikidata.org/sparql",
                           params={"format": "json", "query": req_exclus}, contact=contact)
        a_exclure = {b["item"]["value"].rsplit("/", 1)[1] for b in exclus["results"]["bindings"]}
        liens = http_json("https://query.wikidata.org/sparql",
                          params={"format": "json", "query": req_racines}, contact=contact)
        natures = http_json("https://query.wikidata.org/sparql",
                            params={"format": "json", "query": req_p31}, contact=contact)
        trouves, p31 = {}, {}
        for b in liens["results"]["bindings"]:
            q = b["item"]["value"].rsplit("/", 1)[1]
            trouves.setdefault(q, set()).add(toutes[b["racine"]["value"].rsplit("/", 1)[1]])
        for b in natures["results"]["bindings"]:
            q = b["item"]["value"].rsplit("/", 1)[1]
            p31.setdefault(q, set()).add(b["p31"]["value"].rsplit("/", 1)[1])
        for q in lot:
            type_carte = None if q in a_exclure else next((t for t in TYPES if t in trouves.get(q, ())), None)
            res[q] = (type_carte, sorted(p31.get(q, ())))
        time.sleep(1)
    return res


def resume(langue, titre, contact):
    url = (f"https://{langue}.wikipedia.org/api/rest_v1/page/summary/"
           + urllib.parse.quote(titre.replace(" ", "_"), safe=""))
    rep = http_json(url, contact=contact)
    return (rep or {}).get("extract", "")


def deja_tires(chemins):
    vus = set()
    for c in chemins:
        with open(c, encoding="utf-8") as f:
            for ligne in f:
                if ligne.strip():
                    vus.add(json.loads(ligne)["article"])
    return vus


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--langue", choices=["fr", "en"], required=True)
    p.add_argument("--mois", help="AAAA-MM, par défaut le mois précédent")
    p.add_argument("--par-type", type=int, default=10, help="articles à garder par type de carte")
    p.add_argument("--exclure", nargs="*", default=[], help="fichiers JSONL dont on ignore les articles")
    p.add_argument("--sortie", required=True)
    p.add_argument("--contact", default=CONTACT, help="contact mis dans le User-Agent")
    a = p.parse_args()

    annee, mois = map(int, a.mois.split("-")) if a.mois else mois_precedent()
    vus = deja_tires(a.exclure)

    print(f"Top des articles {a.langue} pour {annee}-{mois:02d}...", file=sys.stderr)
    top = top_articles(a.langue, annee, mois, a.contact)
    print(f"{len(top)} candidats, recherche des QID...", file=sys.stderr)
    q_par_titre = qids(a.langue, [t["titre"] for t in top], a.contact)
    candidats = [(t, q_par_titre[t["titre"]]) for t in top if q_par_titre.get(t["titre"])]

    print(f"{len(candidats)} avec QID, classification Wikidata par lots...", file=sys.stderr)
    compte = {t: 0 for t in TYPES}
    sortie = []
    for debut in range(0, len(candidats), TAILLE_LOT):
        lot = candidats[debut:debut + TAILLE_LOT]
        info = types_wikidata([q for _, q in lot], a.contact)
        for t, q in lot:  # déjà trié par lectures décroissantes
            type_carte, p31 = info[q]
            if type_carte is None or q in vus or compte[type_carte] >= a.par_type:
                continue
            compte[type_carte] += 1
            sortie.append({
                "article": q, "langue": a.langue, "titre": t["titre"], "type": type_carte,
                "fiche": {"resume": resume(a.langue, t["titre"], a.contact),
                          "p31": p31, "lectures": t["lectures"]},
                "attendu": [], "annotateur": None, "difficile": False,
            })
            time.sleep(0.1)
        print(f"  {debut + len(lot)} classés : {compte}", file=sys.stderr)
        if all(c >= a.par_type for c in compte.values()):
            break

    with open(a.sortie, "w", encoding="utf-8") as f:
        for ligne in sortie:
            f.write(json.dumps(ligne, ensure_ascii=False) + "\n")
    print(f"{len(sortie)} articles écrits dans {a.sortie} : {compte}", file=sys.stderr)
    manquants = [t for t, c in compte.items() if c < a.par_type]
    if manquants:
        print(f"Types incomplets (le top mensuel est limité à 1000 articles) : {manquants}", file=sys.stderr)


if __name__ == "__main__":
    main()
