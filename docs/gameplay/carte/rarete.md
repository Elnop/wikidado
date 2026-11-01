# Rareté des cartes

La rareté d'une carte vient de la popularité de son article. Elle n'est pas écrite sur la carte : elle se voit au style de la carte (voir `gameplay/carte/face.md`). Elle détermine la puissance de la carte par rapport à son coût (multiplicateur de budget, voir `gameplay/carte/budget.md`).

## Mesure de la popularité

On mesure la popularité avec les lectures sur 30 jours, additionnées sur toutes les éditions linguistiques de Wikipédia où l'article existe. Le nombre de langues lui-même n'entre pas dans le calcul.

Les lectures de chaque édition s'obtiennent avec l'API Pageviews ou les dumps de pageviews (voir `wikipedia/donnees.md`). On passe d'un article fr à ses équivalents dans les autres langues avec les interwikis ou l'élément Wikidata.

## Paliers

Paliers provisoires, calés sur les lectures de la Wikipédia française seule (échantillon de `wikipedia/donnees.md`). Ils seront plus hauts une fois toutes les langues additionnées, il faudra les recalculer :

| Rareté | Lectures sur 30 jours | Exemples mesurés |
|---|---|---|
| Commune | moins de 100 | Linothele molleturo (0), NGC 4266 (7), William Empson (63) |
| Peu commune | 100 et plus | Caribou (180), Nabih Berri (678), Marcel Ophuls (897) |
| Rare | 5 000 et plus | Irène Jacob (18 353), Michèle Laroque (31 205) |
| Mythique | 50 000 et plus | Napoléon Ier (environ 76 000) |

Il faudra recaler les paliers sur un vrai échantillon pour obtenir la répartition voulue (par exemple 60 % de communes, 25 % de peu communes, 12 % de rares, 3 % de mythiques).

## Saisons

La rareté est figée au début d'une saison (instantané des lectures à une date), sinon les cartes changent de puissance toutes seules.
