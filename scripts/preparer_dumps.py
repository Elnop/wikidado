#!/usr/bin/env python3
"""Classe tous les articles d'un wiki par lectures du mois, à partir de deux dumps.

Entrées (voir docs/wikipedia/api.md, section Dumps) :
  --page-props : frwiki-latest-page_props.sql.gz   (identifiant de page -> QID Wikidata)
  --lectures   : pageviews-AAAAMM-user.bz2         (lectures mensuelles de tous les wikis)

Sortie : un fichier TSV trié par lectures décroissantes, une ligne par article :
  lectures <tab> QID <tab> titre

Les pages hors espace principal (Wikipédia:, Spécial:, Catégorie:...) et les pages
sans QID sont écartées. Les lectures de plusieurs modes d'accès sont additionnées.

Usage :
  python3 scripts/preparer_dumps.py --page-props .dumps/frwiki-page_props.sql.gz \\
      --lectures .dumps/pageviews-202610-user.bz2 --projet fr.wikipedia \\
      --sortie .dumps/fr-2026-10.tsv
"""

import argparse
import bz2
import collections
import gzip
import re
import sys

RE_QID = re.compile(r"^\((\d+),'wikibase_item','(Q\d+)',")
# "Wikipédia:Accueil", "Spécial:Recherche" : un seul mot avant les deux-points.
# "Star_Wars:_Episode_I" garde un underscore avant, donc reste un article.
RE_ESPACE_DE_NOM = re.compile(r"^[^_:]+:")


def lire_qids(chemin):
    qids = {}
    with gzip.open(chemin, "rt", encoding="utf-8", errors="replace") as f:
        for ligne in f:
            m = RE_QID.match(ligne)
            if m:
                qids[int(m.group(1))] = m.group(2)
    return qids


def lire_lectures(chemin, projet):
    """page_id -> (titre, lectures du mois)"""
    vues = collections.Counter()
    titres = {}
    meilleure_ligne = {}  # plusieurs redirections partagent un page_id : on garde le titre le plus lu
    prefixe = projet + " "
    with bz2.open(chemin, "rt", encoding="utf-8", errors="replace") as f:
        for ligne in f:
            if not ligne.startswith(prefixe):
                continue
            champs = ligne.split(" ")
            if len(champs) < 5 or not champs[2].isdigit():
                continue
            page_id = int(champs[2])
            n = int(champs[4])
            if n > meilleure_ligne.get(page_id, -1):
                meilleure_ligne[page_id] = n
                titres[page_id] = champs[1]
            vues[page_id] += n
    return titres, vues


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--page-props", required=True)
    p.add_argument("--lectures", required=True)
    p.add_argument("--projet", default="fr.wikipedia")
    p.add_argument("--sortie", required=True)
    a = p.parse_args()

    print("Lecture de page_props...", file=sys.stderr)
    qids = lire_qids(a.page_props)
    print(f"  {len(qids)} pages avec un QID", file=sys.stderr)

    print("Lecture des lectures mensuelles (long : fichier bz2 de plusieurs Go)...", file=sys.stderr)
    titres, vues = lire_lectures(a.lectures, a.projet)
    print(f"  {len(vues)} pages lues dans {a.projet}", file=sys.stderr)

    lignes = []
    for page_id, n in vues.items():
        qid = qids.get(page_id)
        titre = titres[page_id]
        if qid and not RE_ESPACE_DE_NOM.match(titre):
            lignes.append((n, qid, titre.replace("_", " ")))
    lignes.sort(reverse=True)

    with open(a.sortie, "w", encoding="utf-8") as f:
        for n, qid, titre in lignes:
            f.write(f"{n}\t{qid}\t{titre}\n")
    print(f"{len(lignes)} articles écrits dans {a.sortie}", file=sys.stderr)


if __name__ == "__main__":
    main()
