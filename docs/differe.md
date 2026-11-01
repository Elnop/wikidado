# Travaux différés

Sujets mis de côté volontairement, à reprendre plus tard. Chaque entrée dit quand elle a été différée, jusqu'à quand, et quelle spec elle concerne.

## Équilibre de la courbe de mana

- Différé le 01/11/2026, jusqu'après la première version
- Spec : `gameplay/carte/cout.md`

Le coût d'une carte se déduit de son budget de base, calculé à partir de l'article. On ne choisit donc pas directement combien de cartes coûtent 1, 2, 3... Il faudra vérifier que la répartition des coûts donne des decks jouables.

Pistes :

- mesurer la répartition des coûts sur un pool généré, puis ajuster la formule du budget de base et `points_par_mana`
- imposer des quotas par coût à la validation, et régénérer les cartes d'un coût trop représenté

## Illustration par défaut d'une carte à deux grandes familles

- Différé le 01/11/2026, à décider
- Spec : `gameplay/carte/illustration.md`

L'illustration par défaut dépend du type et de la grande famille, mais une carte peut avoir deux grandes familles (voir `gameplay/carte/famille.md`). Il faut choisir laquelle sert pour l'illustration.

Proposition : prendre la famille la plus représentée parmi les sous-types de la carte.
