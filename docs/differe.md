# Travaux différés

Sujets mis de côté volontairement, à reprendre plus tard. Chaque entrée dit quand elle a été différée, jusqu'à quand, et quelle spec elle concerne.

## Équilibre de la courbe de coûts

- Différé le 01/11/2026, jusqu'après la première version
- Spec : `gameplay/carte/cout.md`

Le coût d'une carte se déduit de son budget de base, calculé à partir de l'article. On ne choisit donc pas directement combien de cartes coûtent 1, 2, 3... Il faudra vérifier que la répartition des coûts donne des decks jouables.

Pistes :

- mesurer la répartition des coûts sur un pool généré, puis ajuster la formule du budget de base et `points_par_electricite`
- imposer des quotas par coût à la validation, et régénérer les cartes d'un coût trop représenté

## Garde-fou sur les rares en construction de deck

- Différé le 01/11/2026, à voir en partie de test
- Spec : aucune pour l'instant (pas de règle de construction de deck)

Les rares sont plus fortes à coût égal (voir `gameplay/carte/budget.md`), donc un deck rempli de mythiques pourrait écraser tout le reste. On verra en partie de test si c'est un vrai problème.

Pistes :

- limite d'exemplaires par rareté dans un deck (Hearthstone autorise une seule copie d'une légendaire)
- limite du nombre total de rares et mythiques par deck
- formats de jeu par rareté, comme le Pauper de Magic où seules les communes sont autorisées

## Internationalisation

- Différé le 01/11/2026, jusqu'après la première version
- Specs : `generation/pipeline.md`, `generation/echantillon.md`, `generation/article/selection.md`

La première version ne prend que des articles de la Wikipédia française. Ensuite, il faudra ouvrir le jeu à d'autres langues, en commençant par l'anglais. Questions à trancher à ce moment-là :

- une carte par élément Wikidata, ou une carte par article de chaque langue
- le modèle d'assignation doit-il être multilingue, et faut-il un échantillon annoté par langue ? Les articles en anglais ont-ils les mêmes mécaniques que leur équivalent français ?
- les classes retenues et les volumes de `generation/article/selection.md` sont mesurés sur fr seulement

Le script `scripts/tirer_echantillon.py` accepte déjà `--langue en`.

## Collection persistante

- Différé le 01/11/2026, jusqu'après la première version
- Spec : `gameplay/collection.md`

En première version, tout le monde a toutes les cartes et les boosters ne sont pas enregistrés. Ensuite, il faudra décider si les joueurs gagnent et gardent leurs cartes, et comment : paquets gratuits à intervalle fixe comme WikiMasters (voir `wikimaster/analyse.md`), paquets gagnés en jouant, échanges entre joueurs.
