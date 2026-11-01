# Stats des cartes

## Principe

La popularité de l'article fixe la rareté de la carte et sa puissance par rapport à son coût : à coût égal, une carte populaire est plus forte qu'une carte obscure. Le coût lui-même est décrit dans `cardcost.md`.

C'est le fonctionnement de Magic : les rares et mythiques y sont souvent plus efficaces que les communes au même coût. Une Napoléon à 4 mana sera meilleure qu'une araignée inconnue à 4 mana, mais elle reste une carte à 4 mana qu'on ne joue pas au tour 1.

## Budget de stats

Comme dans Magic où une créature à N mana a environ N+1 en force + endurance sans capacité, chaque coût donne un budget de base, multiplié selon la rareté :

```
budget = (2 * cout + 1) * multiplicateur_rarete
```

Multiplicateurs de départ, à régler en partie de test :

| Rareté | Multiplicateur |
|---|---|
| Commune | 1,0 |
| Peu commune | 1,1 |
| Rare | 1,25 |
| Mythique | 1,4 |

Une commune à 3 a 7 points à répartir, une mythique à 3 en a environ 10. Une capacité coûte des points de budget.

## Rareté à partir des lectures

On mesure la popularité avec les lectures sur 30 jours, en échelle log, éventuellement combinées au nombre de langues (plus stable que les lectures).

Paliers de départ pour la Wikipédia française, calés sur l'échantillon de `Wikipedia/donnees-disponibles.md` :

| Rareté | Lectures sur 30 jours | Exemples mesurés |
|---|---|---|
| Commune | moins de 100 | Linothele molleturo (0), NGC 4266 (7), William Empson (63) |
| Peu commune | 100 et plus | Caribou (180), Nabih Berri (678), Marcel Ophuls (897) |
| Rare | 5 000 et plus | Irène Jacob (18 353), Michèle Laroque (31 205) |
| Mythique | 50 000 et plus | Napoléon Ier (environ 76 000) |

Il faudra recaler les paliers sur un vrai échantillon pour obtenir la répartition voulue (par exemple 60 % de communes, 25 % de peu communes, 12 % de rares, 3 % de mythiques).

La rareté est figée au début d'une saison (instantané des lectures à une date), sinon les cartes changent de puissance toutes seules.

## Répartition attaque / défense

Les données de l'article décident de la répartition du budget :

- attaque : taille de l'article (ce que le sujet "a à dire")
- défense : nombre de contributeurs (un article défendu par beaucoup de monde est solide)

On compare l'article à la médiane des articles de même coût. Un article plus long que la médiane penche vers l'attaque, un article avec plus de contributeurs penche vers la défense. Pour Napoléon, 260 Ko et 1 944 contributeurs : les deux sont très hauts, donc carte équilibrée. Un article court mais très contributé donnerait un mur défensif.

## Garde-fou sur les rares

Si les rares sont plus fortes à coût égal, un deck rempli de mythiques écrase tout. Pistes :

- limite d'exemplaires par rareté dans un deck (Hearthstone autorise une seule copie d'une légendaire)
- limite du nombre total de rares et mythiques par deck
- formats de jeu par rareté, comme le Pauper de Magic où seules les communes sont autorisées

## Autres données disponibles pour les capacités

- label "Article de qualité" ou "Bon article" : mot-clé de rareté ou capacité bonus (6 600 articles sur fr, assez rare pour être spécial)
- âge de l'article (création en 2003 pour Napoléon) : mot-clé "Ancien" ?
- coordonnées GPS : l'article est un lieu, voir `cardsynergie.md` pour les terrains
- importance "maximum" dans un projet : carte iconique de sa famille

## Bonus d'actualité

Les lectures quotidiennes permettent un effet "Tendance" : si l'article d'une carte est dans le top des plus lus de la semaine, la carte gagne un bonus en jeu (+1/+1, ou coût réduit de 1). La méta bouge avec l'actualité sans toucher à la rareté figée pour la saison.

## Questions ouvertes

- Que faire des articles à 0 langue et 0 lecture (des milliers d'espèces et de communes) : communes, ou on les exclut ?
- Lectures de la Wikipédia française ou anglaise ? L'anglaise est plus stable statistiquement, la française colle mieux au public visé.
- Le nombre de langues compte-t-il dans la popularité, ou seulement les lectures ?
