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
