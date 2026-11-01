# Idées écartées : coût

Idées écartées liées à `../cardcost.md`. On les garde pour savoir ce qui a déjà été envisagé et pourquoi on l'a abandonné.

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

La formule de notoriété peut resservir pour la rareté (voir `../cardrarete.md`).

## Coûts figés pour une saison

Écartée le 01/11/2026 : sans objet depuis que le coût ne dépend plus des lectures. Remplacée par "rareté figée pour une saison", dans `../cardrarete.md`.

L'idée était de prendre un instantané des lectures au début de chaque saison pour calculer les coûts, pour éviter que les decks changent tout seuls d'un jour à l'autre.
