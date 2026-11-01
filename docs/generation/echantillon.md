# Échantillon annoté

Petit jeu d'articles que Leon et Dani annotent à la main avec les mécaniques qu'ils donneraient (voir `gameplay/mecanique.md`). Il sert à comparer les moteurs d'assignation listés dans `generation/pipeline.md` : on mesure le taux d'accord de chaque moteur avec nos choix.

## Ce qu'on mesure

Le type, la rareté et la famille viennent du code (Wikidata et métriques), pas du modèle. L'échantillon ne teste donc que l'assignation : quelles mécaniques du catalogue conviennent à l'article, avec quels paramètres.

Comme le catalogue n'est pas validé, l'échantillon dépend de lui. Si le catalogue change, il faut réannoter les articles concernés.

## Format

Un fichier JSON par ligne (JSON Lines), un article par ligne. Les champs `fiche` et `type` sont remplis par le code, `attendu` par nous.

```json
{
  "article": "Q517",
  "langue": "fr",
  "titre": "Napoléon Ier",
  "type": "creature",
  "fiche": { "resume": "...", "p31": ["Q5"], "lectures": 1200000 },
  "attendu": [
    { "id": "inspiration", "params": { "cible": "histoire" } },
    { "id": "robuste" }
  ],
  "annotateur": "leon",
  "difficile": false
}
```

- `attendu` peut être vide : une carte sans mécanique est valide.
- `difficile` signale un article où plusieurs choix se défendent, pour les isoler dans les mesures.
- Les mécaniques à paramètres tirés des données (`terre-natale`, `participant`) ne sont pas annotées, le code les ajoute seul.

## Composition (piste)

- 200 à 300 articles de la Wikipédia française.
- Réparti sur les 6 types de carte, avec au moins 40 articles par type, pour que chaque type soit mesurable.
- Mélange de rarités, y compris beaucoup d'articles pauvres en données, puisque ce sera la majorité du pool.
- Premier lot : les articles les plus lus du mois, par type, avec `scripts/tirer_echantillon.py`. Ils sont connus de tout le monde, donc faciles à annoter. Les lots suivants doivent venir d'un tirage au hasard dans chaque classe retenue (voir `generation/article/selection.md`), sinon l'échantillon ne représente pas le pool.
- Un tiers mis de côté pour tester, jamais utilisé comme exemples pour le kNN.

## Script de tirage

Deux scripts, qui s'appuient sur les dumps (voir `wikipedia/api.md`) plutôt que sur des milliers d'appels :

```
python3 scripts/preparer_dumps.py --page-props .dumps/frwiki-page_props.sql.gz \
    --lectures .dumps/pageviews-202610-user.bz2 --sortie .dumps/fr-2026-10.tsv
python3 scripts/tirer_echantillon.py --classement .dumps/fr-2026-10.tsv \
    --langue fr --par-type 10 --sortie echantillon/echantillon-fr.jsonl
```

- `preparer_dumps.py` croise le dump `page_props` (identifiant de page vers QID Wikidata) et le dump des lectures mensuelles. Il écrit tous les articles de la Wikipédia, triés par lectures. Il n'y a donc plus de plafond à 1 000 articles.
- `tirer_echantillon.py` parcourt ce classement du plus lu au moins lu, classe les articles par lots de 50 avec l'API `wbgetentities` de Wikidata (classes `P31`, puis `P279`), et s'arrête quand chaque type a `--par-type` articles. Il garde les réponses dans `.cache-echantillon/`, donc une relance est quasi instantanée.
- Les dumps vont dans `.dumps/`, que git ignore.

Le type d'un article suit la règle de `gameplay/carte/type.md` (racine la plus proche). Sont écartés : les œuvres (films, albums, livres, séries, jeux vidéo), les sites web et plateformes, les éléments de fiction, les pages d'homonymie et les listes.

Limites connues :

- les plus lus sont dominés par l'actualité (personnalités politiques, sport, élections) et contiennent des articles sensibles (crimes, meurtriers), gardés comme les autres
- les racines de classes par type sont provisoires
- les types rares dans les plus lus (Objet) demandent d'examiner beaucoup d'articles : `--max-examines` fixe la limite

## Mesures

- accord exact : le moteur propose exactement notre liste
- précision et rappel par mécanique
- accord par type de carte
- part des réponses peu confiantes, et leur accord réel (une confiance faible doit annoncer une erreur)
- temps par carte sur CPU

## Questions ouvertes

- Leon et Dani annotent-ils chacun les mêmes articles, pour mesurer notre propre désaccord ?
- Faut-il annoter avant ou après avoir fixé une première version du catalogue ?
