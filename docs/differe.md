# Travaux différés

Sujets mis de côté volontairement, à reprendre plus tard. Chaque entrée dit quand elle a été différée, jusqu'à quand, et quelle spec elle concerne.

## Équilibre de la courbe de coûts

- Différé le 01/11/2026, jusqu'après la première version
- Spec : `gameplay/carte/cout.md`

Le coût d'une carte se déduit de son budget de base, calculé à partir de l'article. On ne choisit donc pas directement combien de cartes coûtent 1, 2, 3... Il faudra vérifier que la répartition des coûts donne des decks jouables.

Pistes :

- mesurer la répartition des coûts sur un pool généré, puis ajuster la formule du budget de base et `points_par_electricite`
- imposer des quotas par coût à la validation, et régénérer les cartes d'un coût trop représenté

## Illustration par défaut d'une carte à plusieurs grandes familles

- Différé le 01/11/2026, à décider
- Spec : `gameplay/carte/illustration.md`

L'illustration par défaut dépend du type et de la grande famille, mais une carte appartient à toutes les grandes familles de ses sous-types, sans limite (voir `gameplay/carte/famille.md`). Il faut choisir laquelle sert pour l'illustration.

Proposition : prendre la grande famille qui regroupe le plus de sous-types de la carte.

## Œuvres comme cartes

- Différé le 01/11/2026, jusqu'à ce que les 4 types soient vérifiés
- Specs : `gameplay/carte/type.md`, `generation/article/selection.md`

Les films, albums, livres et singles sont exclus pour la première version. Il faudra décider s'ils deviennent des cartes, et dans quel type. Il y a du volume : 29 427 albums et 10 664 singles sur la Wikipédia française, sans compter les films et les livres.

## Garde-fou sur les rares en construction de deck

- Différé le 01/11/2026, à voir en partie de test
- Spec : aucune pour l'instant (pas de règle de construction de deck)

Les rares sont plus fortes à coût égal (voir `gameplay/carte/budget.md`), donc un deck rempli de mythiques pourrait écraser tout le reste. On verra en partie de test si c'est un vrai problème.

Pistes :

- limite d'exemplaires par rareté dans un deck (Hearthstone autorise une seule copie d'une légendaire)
- limite du nombre total de rares et mythiques par deck
- formats de jeu par rareté, comme le Pauper de Magic où seules les communes sont autorisées

## Planche d'exemples de cartes

- Noté le 01/11/2026, à produire quand les specs seront assez stables
- Specs : toutes celles de `gameplay/`

Produire un design (Claude Design) qui montre des exemples de cartes construites à partir de vrais articles (Napoléon Ier, la Tour Eiffel, la Bataille d'Austerlitz, une espèce peu connue...). Pour chaque carte, expliquer ce qui la définit : type et sous-types, familles, budget de base et son calcul, coût en électricité, rareté et bonus de budget, mécaniques choisies et leur `cout_budget`, stats, illustration.
