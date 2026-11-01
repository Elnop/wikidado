# Coût des cartes

Proposition de départ, à discuter avec Dani.

## Le problème à éviter

Chez WikiMasters, les stats montent avec la notoriété, donc la carte la plus célèbre gagne. Dans Magic, une carte puissante coûte cher et une carte à 1 mana a sa place dans un deck. On veut garder ça.

D'où la règle de base : la notoriété de l'article fixe le coût. Le reste des données décide de la façon dont ce coût est dépensé (répartition attaque/défense, capacités). Une carte à 2 et une carte à 6 sont toutes les deux équilibrées pour leur coût.

## Calcul du coût

On mesure la notoriété avec deux données qui se complètent : les lectures (popularité actuelle) et le nombre de langues (importance dans le monde, plus stable).

```
notoriete = log10(lectures_30j + 1) + 0.5 * log2(langues + 1)
cout = clamp(round(notoriete * 0.75), 1, 7)
```

Sur les articles mesurés :

| Article | Lectures 30 j | Langues | Notoriété | Coût |
|---|---|---|---|---|
| Linothele molleturo | 0 | 0 | 0 | 1 |
| District de Koraput | 3 | 33 | 3,1 | 2 |
| NGC 4266 | 7 | 24 | 3,2 | 2 |
| Musaraigne sombre | 13 | 27 | 3,5 | 3 |
| William Empson | 63 | 17 | 3,9 | 3 |
| Caribou (musicien) | 180 | 13 | 4,2 | 3 |
| Nabih Berri | 678 | 21 | 5,1 | 4 |
| Marcel Ophuls | 897 | 26 | 5,3 | 4 |
| Michèle Laroque | 31 205 | 24 | 6,8 | 5 |
| Irène Jacob | 18 353 | 37 | 6,9 | 5 |
| Napoléon Ier | ~76 000 | 221 | 8,8 | 7 |

La courbe donne beaucoup de cartes à 2-3 et peu de cartes à 6-7, ce qui ressemble à une courbe de mana normale. Les coefficients sont à ajuster une fois qu'on aura un vrai échantillon de quelques milliers d'articles.

Les lectures varient d'un jour à l'autre. Le coût doit être figé au début d'une saison (instantané des lectures à une date), sinon les decks changent tout seuls. L'actualité peut passer par un bonus temporaire séparé (voir plus bas).

## Budget de stats

Comme dans Magic où une créature à N mana a environ N+1 en force + endurance sans capacité, chaque coût donne un budget :

```
budget = 2 * cout + 1
```

Une carte à 3 a 7 points à répartir entre attaque et défense. Une capacité coûte des points de budget.

## Répartition attaque / défense

C'est là que les données de l'article reprennent la main, en relatif, à notoriété égale :

- attaque : taille de l'article (ce que le sujet "a à dire")
- défense : nombre de contributeurs (un article défendu par beaucoup de monde est solide)

On compare l'article à la médiane des articles de même coût. Un article plus long que la médiane penche vers l'attaque, un article avec plus de contributeurs penche vers la défense. Pour Napoléon, 260 Ko et 1 944 contributeurs : les deux sont très hauts, donc carte équilibrée. Un article court mais très contributé donnerait un mur défensif.

## Autres données disponibles pour les capacités

- label "Article de qualité" ou "Bon article" : mot-clé de rareté ou capacité bonus (6 600 articles sur fr, assez rare pour être spécial)
- âge de l'article (création en 2003 pour Napoléon) : mot-clé "Ancien" ?
- coordonnées GPS : l'article est un lieu, voir `cardsynergie.md` pour les terrains
- importance "maximum" dans un projet : carte iconique de sa famille

## Rareté

On peut garder la rareté séparée du coût, sur les lectures comme WikiMasters, ou la dériver du coût. Je préfère la séparer : une carte à 2 très lue (sujet d'actu dont l'article est court et traduit dans peu de langues) peut être rare sans être chère.

## Bonus d'actualité

Les lectures quotidiennes permettent un effet "Tendance" : si l'article d'une carte est dans le top des plus lus de la semaine, la carte gagne un bonus en jeu (+1/+1, ou coût réduit de 1). La méta bouge avec l'actualité sans toucher aux coûts de base.

## Questions ouvertes

- Un seul type de mana générique, ou du mana coloré par famille de portails ?
- Coût de 1 à 7 ou plus large ?
- Que faire des articles à 0 langue et 0 lecture (des milliers d'espèces et de communes) : cartes à 1, ou on les exclut ?
- Lectures de la Wikipédia française ou anglaise ? L'anglaise est plus stable statistiquement, la française colle mieux au public visé.
