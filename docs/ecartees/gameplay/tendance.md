# Idées écartées : tendance

## Bonus de tendance

Écartée le 01/11/2026 : trop volatile, le jeu n'est pas mis à jour chaque semaine.

Les lectures quotidiennes permettent un effet "Tendance" : si l'article d'une carte est dans le top des plus lus de la semaine, la carte gagne un bonus en jeu (+1/+1, ou coût réduit de 1). La méta bouge avec l'actualité sans toucher à la rareté, qui reste figée pour la saison (voir `gameplay/carte/rarete.md`).

Source des données : flux "le plus lu" de `/api/rest_v1/feed/featured/{aaaa}/{mm}/{jj}` ou top mensuel de l'API Pageviews (voir `wikipedia/donnees.md`).

Bonus envisagés : +1/+1 (seulement pour les Créatures), coût réduit de 1, ou traitement comme une rareté au-dessus tant que la carte est en tendance.
