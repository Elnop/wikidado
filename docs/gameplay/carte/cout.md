# Coût des cartes

## Principe

Le coût d'une carte se déduit de son budget de base (voir `gameplay/carte/budget.md`). Le budget vient de données de l'article sans lien avec sa popularité, donc le coût ne dépend pas de la popularité non plus. La popularité fixe la rareté (voir `gameplay/carte/rarete.md`), qui ajoute du budget sans changer le coût.

Le coût se paie en électricité (voir `gameplay/electricite.md`). Une carte puissante coûte cher, et une carte à 1 électricité a sa place dans un deck. Il n'y a qu'une seule ressource, quelle que soit la famille de la carte.

## Calcul

```
cout = arrondi(budget_base / points_par_electricite)
```

`points_par_electricite` vaut 1,5 pour commencer, à régler en partie de test. Avec cette valeur, les coûts vont de 0 à 10 : un article médian (budget 4) coûte 3, Napoléon Ier (budget 13) coûte 9, les plus gros articles de la Wikipédia française (budget 15) coûtent 10. Les coûts couvrent ainsi toute la réserve d'électricité, qui monte jusqu'à 10 (voir `gameplay/electricite.md`).

Le coût se calcule sur le budget de base, avant le bonus de rareté. Deux cartes de même budget de base ont le même coût, même si l'une est mythique et l'autre commune.

Il n'y a pas de coût de base selon le type. Le coût minimum est 0. Il n'y a pas de coût maximum.
