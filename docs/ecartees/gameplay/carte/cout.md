# Idées écartées : coût

Idées écartées liées à `gameplay/carte/cout.md`. On les garde pour savoir ce qui a déjà été envisagé et pourquoi on l'a abandonné.

## Coût fixé par la notoriété

Écartée le 01/11/2026 : le coût ne doit pas dépendre de la popularité. La popularité fixe la rareté et la puissance par rapport au coût.

On mesurait la notoriété avec les lectures et le nombre de langues :

```
notoriete = log10(lectures_30j + 1) + 0.5 * log2(langues + 1)
cout = clamp(round(notoriete * 0.75), 1, 7)
```

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

La formule de notoriété peut resservir pour la rareté (voir `gameplay/carte/rarete.md`).

## Coûts figés pour une saison

Écartée le 01/11/2026 : sans objet depuis que le coût ne dépend plus des lectures. Remplacée par "rareté figée pour une saison", dans `gameplay/carte/rarete.md`.

L'idée était de prendre un instantané des lectures au début de chaque saison pour calculer les coûts, pour éviter que les decks changent tout seuls d'un jour à l'autre.

## Coût tiré d'une donnée de l'article

Écartée le 01/11/2026 : le coût découle des mécaniques assignées.

Le coût venait d'une donnée de l'article sans lien avec la popularité, par exemple la taille de l'article (un sujet "lourd" coûte cher) ou le nombre de liens sortants. Si la taille de l'article fixait le coût, elle ne pouvait plus servir pour l'attaque.

## Coût selon le type et la nature Wikidata

Écartée le 01/11/2026 : le coût découle des mécaniques assignées.

Le coût dépendait du type et de la nature Wikidata : une bataille coûte plus qu'une escarmouche, une capitale plus qu'un village.

## Coût tiré pour équilibrer la courbe de mana

Écartée le 01/11/2026 : le coût découle des mécaniques assignées.

Le coût était tiré pour obtenir une courbe de mana équilibrée dans chaque famille, puis le reste de la carte s'adaptait.

## Mana coloré par famille

Écartée le 01/11/2026 : le mana est générique.

Tout le coût d'une carte se payait avec le mana de sa famille. Contraignant, les decks à plusieurs familles devenaient durs à jouer.

## Mana générique et mana coloré

Écartée le 01/11/2026 : le mana est générique.

Comme Magic : un coût mélangeait du mana générique et du mana de la famille de la carte (par exemple 2 + 1 Histoire). Les familles comptaient dans la construction de deck.

## Coût de base selon le type

Écartée le 01/11/2026 : pas de coût de base, le coût minimum est 0.

Chaque type avait un coût de base (par exemple Créature 1, Événement 0), ajouté au coût des mécaniques, pour qu'une créature sans capacité coûte quand même quelque chose. Variante : un coût de base identique pour tous les types.

## Plage de coûts fermée

Écartée le 01/11/2026 : coût minimum 0, pas de maximum.

Plages envisagées : 1 à 7 (lisible, pas de carte gratuite), 1 à 10 (plus de place pour les grosses cartes, comme Hearthstone), 0 à 7 et plus.

## Coût à partir du budget total stats + mécaniques

Écartée le 01/11/2026 : le coût est la somme des cout_budget des mécaniques, convertie en mana.

Le code fixait d'abord les stats voulues à partir de l'article, ajoutait le cout_budget des mécaniques, et le coût était le plus petit coût dont le budget (multiplié par la rareté) couvrait ce total.

## Coût égal à la somme directe des cout_budget

Écartée le 01/11/2026 : le coût est la somme des cout_budget convertie en mana.

Le coût était la somme des cout_budget des mécaniques sans conversion, et les stats venaient d'un budget séparé.

## Stats tirées de l'article et comptées dans le coût

Écartée le 01/11/2026 : les cartes sans capacité passent par des mécaniques de stats.

Le code fixait des stats à partir de l'article (taille, contributeurs), et ces stats comptaient dans le budget qui fixe le coût, comme les mécaniques.

## Pas de carte sans capacité

Écartée le 01/11/2026 : les cartes sans capacité passent par des mécaniques de stats.

Toutes les cartes avaient au moins une capacité. Une carte sans mécanique n'était pas générée.
