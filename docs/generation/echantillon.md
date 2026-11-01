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

- 200 à 300 articles, moitié Wikipédia FR, moitié EN.
- Réparti sur les 4 types de carte, avec au moins 40 articles par type, pour que chaque type soit mesurable.
- Mélange de rarités, y compris beaucoup d'articles pauvres en données, puisque ce sera la majorité du pool.
- Premier lot : les articles les plus lus du mois, par type, avec `scripts/tirer_echantillon.py`. Ils sont connus de tout le monde, donc faciles à annoter. Les lots suivants doivent venir d'un tirage au hasard dans chaque classe retenue (voir `generation/article/selection.md`), sinon l'échantillon ne représente pas le pool.
- Un tiers mis de côté pour tester, jamais utilisé comme exemples pour le kNN.

## Script de tirage

`scripts/tirer_echantillon.py` produit le format ci-dessus (champs `attendu` vides) :

```
python3 scripts/tirer_echantillon.py --langue fr --par-type 10 --sortie echantillon-fr.jsonl
python3 scripts/tirer_echantillon.py --langue en --par-type 10 --exclure echantillon-fr.jsonl --sortie echantillon-en.jsonl
```

Il prend le top mensuel de l'API Pageviews, déduit le type de carte de la classe Wikidata (`P31/P279*`, racines provisoires) et garde les articles dans l'ordre de lecture jusqu'à `--par-type` par type. `--exclure` évite de retirer des articles déjà tirés.

Limites connues :

- le top mensuel est limité à 1000 articles, et un type peut rester incomplet
- les plus lus sont dominés par l'actualité (personnalités politiques, sport, élections) et contiennent des articles sensibles (site pour adultes). Le filtre des articles sensibles de `generation/article/selection.md` n'est pas encore appliqué
- les racines de classes par type sont provisoires : un pays est classé Terrain, et un réseau social ou un site Web, Technique

## Mesures

- accord exact : le moteur propose exactement notre liste
- précision et rappel par mécanique
- accord par langue (FR contre EN) et par type de carte
- part des réponses peu confiantes, et leur accord réel (une confiance faible doit annoncer une erreur)
- temps par carte sur CPU

## Questions ouvertes

- Leon et Dani annotent-ils chacun les mêmes articles, pour mesurer notre propre désaccord ?
- Faut-il annoter avant ou après avoir fixé une première version du catalogue ?
- Les articles en anglais ont-ils les mêmes mécaniques que leur équivalent français, ou le modèle doit-il être testé à part ?
