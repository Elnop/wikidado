# Familles

Une famille est un groupe de sous-types (voir `gameplay/carte/type.md`). Le mana est générique (voir `gameplay/carte/cout.md`), donc les familles ne servent pas à payer les cartes : elles servent aux synergies, avec des effets tribaux ("vos Animaux gagnent +1 en attaque", "vos cartes Histoire et politique gagnent +1 en défense").

## Deux niveaux

Les familles ont deux niveaux :

- des groupes fins, définis à la main, qui réunissent des sous-types proches : Animaux (Cheval, Loup, Aigle...), Militaires (Général, Soldat, Artilleur...), Religieux, Monuments...
- 6 grandes familles, qui réunissent les groupes fins

Les synergies peuvent viser l'un ou l'autre niveau.

Première idée de grandes familles :

- Histoire et politique
- Sciences et techniques
- Arts et culture
- Géographie et lieux
- Nature et vivant
- Sport et loisirs

## Familles d'une carte

Les sous-types d'une carte viennent de Wikidata, donc ses familles aussi. Quand les sous-types d'une carte tombent dans plusieurs familles, on compte les sous-types par famille et on garde les deux familles les plus représentées.

Napoléon a les sous-types Homme politique, Militaire et Monarque (occupations Wikidata). Militaire va dans le groupe Militaires, les deux autres dans un groupe Dirigeants. Les deux groupes sont dans la grande famille Histoire et politique.

## Travail à faire

Lister les sous-types (classes `P31` retenues et occupations `P106`) et les ranger dans les groupes fins, puis les groupes fins dans les grandes familles. La liste des classes est déjà tenue à la main pour la sélection des articles (voir `generation/article/selection.md`).
