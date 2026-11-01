# Coût des cartes

## Principe

Le coût d'une carte ne dépend pas de la popularité de son article. La popularité fixe la rareté et la puissance par rapport au coût, ce qui est décrit dans `cardstats.md`.

Comme dans Magic, une carte puissante coûte cher et une carte à 1 mana a sa place dans un deck.

## Ce qui fixe le coût

Pistes :

- le coût découle de ce que la carte fait : le modèle assigne les mécaniques, le code additionne leur coût et celui des stats voulues. C'est le plus proche de la façon dont on conçoit une carte Magic.
- le coût vient d'une donnée de l'article sans lien avec la popularité, par exemple la taille de l'article (un sujet "lourd" coûte cher) ou le nombre de liens sortants
- le coût dépend du type et de la nature Wikidata : une bataille coûte plus qu'une escarmouche, une capitale plus qu'un village
- le coût est tiré pour obtenir une courbe de mana équilibrée dans chaque famille, puis le reste s'adapte

Si la taille de l'article fixe le coût, elle ne peut plus servir pour l'attaque (voir `cardstats.md`).

## Questions ouvertes

- Qu'est-ce qui fixe le coût ?
- Un seul type de mana générique, ou du mana coloré par famille de portails ?
- Coût de 1 à 7 ou plus large ?
