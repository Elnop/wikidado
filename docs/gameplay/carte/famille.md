# Familles

Chaque carte appartient à une ou deux familles. Le mana est générique (voir `gameplay/carte/cout.md`), donc les familles ne servent pas à payer les cartes : elles servent aux synergies, avec des effets tribaux ("vos cartes Histoire gagnent +1 en attaque").

## Calcul à partir de Wikidata

La famille d'une carte se déduit des données Wikidata de son article :

- la nature de l'élément (`P31`) : une église, un château, une bataille, une espèce
- pour les personnes, l'occupation (`P106`) : homme politique, militaire, peintre, physicien
- quand elle existe, le domaine (`P101`) ou le champ de travail

On range une fois pour toutes ces classes et ces occupations dans les familles. La liste de classes est déjà tenue à la main pour la sélection des articles (voir `generation/article/selection.md`), on peut y ajouter la famille de chaque classe.

Napoléon (être humain, occupations homme politique, militaire, monarque) serait Histoire et politique. La Tour Eiffel (tour) serait Géographie et lieux, et Arts et culture si on range les monuments dans les deux.

## Familles

Première idée de découpage :

- Histoire et politique
- Sciences et techniques
- Arts et culture
- Géographie et lieux
- Nature et vivant
- Sport et loisirs

## Questions ouvertes

- Comment éviter que la famille fasse doublon avec le type de carte ? Avec Wikidata, beaucoup de lieux tomberaient dans Géographie et lieux, et toutes les espèces dans Nature et vivant.
- Quand une personne a plusieurs occupations dans des familles différentes, laquelle prendre ? Les deux, ou la première ?
