# Rareté des cartes

La rareté d'une carte vient de la popularité de son article. Elle détermine la puissance de la carte par rapport à son coût (multiplicateur de budget, voir `carte-stats.md`).

## Mesure de la popularité

On mesure la popularité avec les lectures sur 30 jours, en échelle log, éventuellement combinées au nombre de langues (plus stable que les lectures).

## Paliers

Paliers de départ pour la Wikipédia française, calés sur l'échantillon de `wikipedia/donnees.md` :

| Rareté | Lectures sur 30 jours | Exemples mesurés |
|---|---|---|
| Commune | moins de 100 | Linothele molleturo (0), NGC 4266 (7), William Empson (63) |
| Peu commune | 100 et plus | Caribou (180), Nabih Berri (678), Marcel Ophuls (897) |
| Rare | 5 000 et plus | Irène Jacob (18 353), Michèle Laroque (31 205) |
| Mythique | 50 000 et plus | Napoléon Ier (environ 76 000) |

Il faudra recaler les paliers sur un vrai échantillon pour obtenir la répartition voulue (par exemple 60 % de communes, 25 % de peu communes, 12 % de rares, 3 % de mythiques).

## Saisons

La rareté est figée au début d'une saison (instantané des lectures à une date), sinon les cartes changent de puissance toutes seules.

## Questions ouvertes

- Lectures de la Wikipédia française ou anglaise ? L'anglaise est plus stable statistiquement, la française colle mieux au public visé.
- Le nombre de langues compte-t-il dans la popularité, ou seulement les lectures ?
