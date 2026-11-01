#!/usr/bin/env python3
"""Tire un échantillon d'articles Wikipédia, des plus lus aux moins lus.

Voir docs/generation/echantillon.md pour le format de sortie (JSON Lines).

Étapes :
  1. API Pageviews : top des articles les plus lus du mois (1000 maximum).
  2. API Wikipédia : identifiant Wikidata (QID) de chaque article.
  3. SPARQL Wikidata : type de carte = racine la plus proche des classes P31 (liens P279), classes exclues écartées.
  4. REST summary : résumé de l'article.

Sources de candidats (--source) :
  auto (défaut) : Événement, Objet et Savoir viennent des classes Wikidata (les plus
                  présentes dans les langues, puis lectures du mois), ce qui donne
                  --par-type articles même si le type est rare dans le top. Créature et
                  Terrain, trop gros pour le SPARQL, viennent du top mensuel. Un type en
                  échec retombe sur le top mensuel.
  top           : tout vient du top mensuel de l'API Pageviews (1000 articles au plus).

Les réponses des API sont gardées dans .cache-echantillon/ : une relance est
quasi instantanée. --sans-cache pour tout redemander.

On garde les articles dans l'ordre de lecture, jusqu'à avoir --par-type
articles de chaque type de carte. Les articles sans type reconnu (listes,
œuvres, pages spéciales...) sont ignorés.

Usage :
  python3 scripts/tirer_echantillon.py --langue fr --par-type 10 --sortie echantillon-fr.jsonl
  python3 scripts/tirer_echantillon.py --langue en --exclure echantillon-fr.jsonl ...
"""

import argparse
import calendar
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date

CONTACT = "https://github.com/Elnop/wikidado"
TYPES = ["creature", "terrain", "evenement", "objet", "savoir"]

# Classes racines par type de carte. Provisoire : voir gameplay/carte/type.md et
# generation/article/selection.md. Le type d'un article est celui de la racine la
# plus proche de ses classes P31, en comptant les liens "sous-classe de" (P279).
# À distance égale, l'ordre de TYPES départage.
RACINES = {
    "creature": ["Q5", "Q16521"],  # être humain, taxon
    "terrain": ["Q2221906", "Q41176", "Q811979"],  # lieu, bâtiment, structure architecturale
    "evenement": ["Q1190554", "Q178561", "Q645883"],  # occurrence, bataille, opération militaire
    "objet": [
        "Q39546", "Q728", "Q42889", "Q11019", "Q34379", "Q11460", "Q1183543",
        "Q8205328",  # outil, arme, véhicule, machine, instrument de musique, vêtement, dispositif, objet artificiel
    ],
    "savoir": [
        "Q11862829", "Q336", "Q17737", "Q151885", "Q11016", "Q9143", "Q7397", "Q246672",
        "Q7257", "Q968159",  # discipline, science, théorie, concept, technologie, langage de programmation,
                             # logiciel, objet mathématique, idéologie, mouvement artistique
    ],
}

# Racines assez petites pour chercher les candidats par classe dans le SPARQL Wikidata.
# Les racines trop larges (humains, taxons, lieux, objet artificiel, concept) expirent.
RACINES_CANDIDATS = {
    "evenement": ["Q178561", "Q645883"],
    "objet": ["Q39546", "Q728", "Q42889", "Q11019", "Q34379", "Q11460", "Q1183543"],
    "savoir": ["Q11862829", "Q336", "Q17737", "Q11016", "Q9143", "Q7397", "Q246672", "Q7257", "Q968159"],
}

# Types dont on cherche les candidats par classe. Créature et Terrain passent par le top mensuel.
TYPES_PAR_CLASSES = tuple(RACINES_CANDIDATS)

DOSSIER_CACHE = ".cache-echantillon"
utiliser_cache = True

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
    "Q14897293",   # entité fictionnelle (armes, lieux, personnages inventés)
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
    fichier = None
    if utiliser_cache:
        cle = hashlib.sha1(f"{url}\n{corps}".encode()).hexdigest()
        fichier = os.path.join(DOSSIER_CACHE, cle + ".json")
        if os.path.exists(fichier):
            with open(fichier, encoding="utf-8") as f:
                return json.load(f)
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


def candidats_par_classe(langue, type_carte, par_racine, contact):
    """Articles d'un type, triés par nombre de langues, depuis Wikidata. -> [(titre, qid)]"""
    trouves = {}
    for racine in RACINES_CANDIDATS[type_carte]:
        requete = f"""
SELECT ?item ?titre ?n WHERE {{
  ?item wdt:P31/wdt:P279* wd:{racine} ; wikibase:sitelinks ?n .
  ?a schema:about ?item ; schema:isPartOf <https://{langue}.wikipedia.org/> ; schema:name ?titre .
}} ORDER BY DESC(?n) LIMIT {par_racine}"""
        rep = http_json("https://query.wikidata.org/sparql",
                        params={"format": "json", "query": requete}, contact=contact, essais=1)
        for b in rep["results"]["bindings"]:
            q = b["item"]["value"].rsplit("/", 1)[1]
            trouves[q] = b["titre"]["value"]
        time.sleep(1)
    return [(t, q) for q, t in trouves.items()]


def lectures_mois(langue, titre, annee, mois, contact):
    """Lectures de l'article sur un mois (0 si inconnu)."""
    t = urllib.parse.quote(titre.replace(" ", "_"), safe="")
    url = (f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/"
           f"{langue}.wikipedia/all-access/user/{t}/monthly/{annee}{mois:02d}01/{annee}{mois:02d}{calendar.monthrange(annee, mois)[1]}")
    try:
        rep = http_json(url, contact=contact, essais=2)
    except urllib.error.HTTPError as e:  # titre que l'API refuse : on le compte à 0
        print(f"  lectures impossibles pour {titre!r} ({e.code})", file=sys.stderr)
        return 0
    time.sleep(0.05)
    return rep["items"][0]["views"] if rep and rep.get("items") else 0


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


PARENTS = {}  # classe -> classes parentes (P279), mémoire du processus


def parents_de(classes, contact):
    a_chercher = [c for c in classes if c not in PARENTS]
    for i in range(0, len(a_chercher), 80):
        lot = a_chercher[i:i + 80]
        valeurs = " ".join(f"wd:{c}" for c in lot)
        requete = f"SELECT ?c ?p WHERE {{ VALUES ?c {{ {valeurs} }} ?c wdt:P279 ?p }}"
        rep = http_json("https://query.wikidata.org/sparql",
                        params={"format": "json", "query": requete}, contact=contact)
        for c in lot:
            PARENTS[c] = set()
        for b in rep["results"]["bindings"]:
            PARENTS[b["c"]["value"].rsplit("/", 1)[1]].add(b["p"]["value"].rsplit("/", 1)[1])
        time.sleep(0.5)


def type_le_plus_proche(p31_par_item, contact, profondeur_max=12):
    """QID -> type de la racine la plus proche des classes P31 (None si aucune).

    Recherche en largeur sur les liens P279, niveau par niveau pour tous les
    articles du lot à la fois, avec les parents gardés en mémoire.
    """
    racine_type = {r: t for t, rs in RACINES.items() for r in rs}
    ordre = {t: i for i, t in enumerate(TYPES)}
    res = {q: None for q in p31_par_item}
    front = {q: set(c) for q, c in p31_par_item.items()}
    vus = {q: set(c) for q, c in p31_par_item.items()}
    for _ in range(profondeur_max + 1):
        for q in front:
            if res[q] is None:
                trouves = [racine_type[c] for c in front[q] if c in racine_type]
                if trouves:
                    res[q] = min(trouves, key=ordre.get)
        actifs = [q for q in front if res[q] is None and front[q]]
        if not actifs:
            break
        parents_de(set().union(*(front[q] for q in actifs)), contact)
        for q in actifs:
            suivants = set().union(*(PARENTS[c] for c in front[q])) - vus[q]
            vus[q] |= suivants
            front[q] = suivants
    return res


def types_wikidata(liste_qids, contact):
    """QID -> (type de carte, liste des P31), via SPARQL."""
    res = {}
    for i in range(0, len(liste_qids), TAILLE_LOT):
        lot = liste_qids[i:i + TAILLE_LOT]
        items = " ".join(f"wd:{q}" for q in lot)
        req_exclus = f"""
SELECT DISTINCT ?item WHERE {{
  VALUES ?item {{ {items} }}
  VALUES ?exclu {{ {" ".join("wd:" + e for e in EXCLUSIONS)} }}
  ?item wdt:P31/wdt:P279* ?exclu
}}"""
        req_p31 = f"""
SELECT ?item ?p31 WHERE {{
  VALUES ?item {{ {items} }}
  ?item wdt:P31 ?p31
}}"""
        exclus = http_json("https://query.wikidata.org/sparql",
                           params={"format": "json", "query": req_exclus}, contact=contact)
        natures = http_json("https://query.wikidata.org/sparql",
                            params={"format": "json", "query": req_p31}, contact=contact)
        a_exclure = {b["item"]["value"].rsplit("/", 1)[1] for b in exclus["results"]["bindings"]}
        p31 = {}
        for b in natures["results"]["bindings"]:
            p31.setdefault(b["item"]["value"].rsplit("/", 1)[1], set()).add(b["p31"]["value"].rsplit("/", 1)[1])
        types = type_le_plus_proche({q: p31.get(q, set()) for q in lot if q not in a_exclure}, contact)
        for q in lot:
            res[q] = (types.get(q), sorted(p31.get(q, ())))
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
    p.add_argument("--source", choices=["auto", "top"], default="auto")
    p.add_argument("--sans-cache", action="store_true", help="ignore le cache disque (.cache-echantillon/)")
    p.add_argument("--candidats", type=int, default=150, help="source classes : candidats par classe racine")
    p.add_argument("--par-type", type=int, default=10, help="articles à garder par type de carte")
    p.add_argument("--exclure", nargs="*", default=[], help="fichiers JSONL dont on ignore les articles")
    p.add_argument("--sortie", required=True)
    p.add_argument("--contact", default=CONTACT, help="contact mis dans le User-Agent")
    a = p.parse_args()

    global utiliser_cache
    utiliser_cache = not a.sans_cache
    annee, mois = map(int, a.mois.split("-")) if a.mois else mois_precedent()
    vus = deja_tires(a.exclure)

    compte = {t: 0 for t in TYPES}
    sortie = []

    def garder(t, q, type_carte, p31, lectures):
        compte[type_carte] += 1
        sortie.append({
            "article": q, "langue": a.langue, "titre": t, "type": type_carte,
            "fiche": {"resume": resume(a.langue, t, a.contact), "p31": p31, "lectures": lectures},
            "attendu": [], "annotateur": None, "difficile": False,
        })
        time.sleep(0.1)

    top_cache = []

    def depuis_top(type_carte):
        """Articles du top mensuel qui ont ce type -> [(lectures, titre, qid, p31)]"""
        if not top_cache:
            print(f"Top des articles {a.langue} pour {annee}-{mois:02d}...", file=sys.stderr)
            top = top_articles(a.langue, annee, mois, a.contact)
            q_par_titre = qids(a.langue, [t["titre"] for t in top], a.contact)
            cands = [(t, q_par_titre[t["titre"]]) for t in top if q_par_titre.get(t["titre"])]
            for debut in range(0, len(cands), TAILLE_LOT):
                lot = cands[debut:debut + TAILLE_LOT]
                info = types_wikidata([q for _, q in lot], a.contact)
                top_cache.extend((t["lectures"], t["titre"], q, info[q][0], info[q][1]) for t, q in lot)
                if len(top_cache) % 100 == 0:
                    print(f"  {len(top_cache)} classés", file=sys.stderr)
        return [(l, t, q, p31) for l, t, q, ty, p31 in top_cache if ty == type_carte and q not in vus]

    for type_carte in TYPES:
        avec = None
        if a.source == "auto" and type_carte in TYPES_PAR_CLASSES:
            print(f"{type_carte} : recherche des candidats par classe...", file=sys.stderr)
            try:
                cands = [(t, q) for t, q in candidats_par_classe(a.langue, type_carte, a.candidats, a.contact)
                         if q not in vus]
                info = types_wikidata([q for _, q in cands], a.contact)
                cands = [(t, q) for t, q in cands if info[q][0] == type_carte]
                print(f"  {len(cands)} candidats retenus, lectures du mois...", file=sys.stderr)
                avec = sorted(((lectures_mois(a.langue, t, annee, mois, a.contact), t, q, info[q][1])
                               for t, q in cands), reverse=True)
            except OSError as e:
                print(f"  requête impossible ({e}), repli sur le top mensuel", file=sys.stderr)
        if avec is None:
            avec = sorted(depuis_top(type_carte), reverse=True)
        for lectures, t, q, p31 in avec[:a.par_type]:
            garder(t, q, type_carte, p31, lectures)
        print(f"  {compte[type_carte]} gardés", file=sys.stderr)

    with open(a.sortie, "w", encoding="utf-8") as f:
        for ligne in sortie:
            f.write(json.dumps(ligne, ensure_ascii=False) + "\n")
    print(f"{len(sortie)} articles écrits dans {a.sortie} : {compte}", file=sys.stderr)
    manquants = [t for t, c in compte.items() if c < a.par_type]
    if manquants:
        print(f"Types incomplets (pas assez de candidats) : {manquants}", file=sys.stderr)


if __name__ == "__main__":
    main()
