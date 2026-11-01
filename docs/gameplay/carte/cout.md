# Coût des cartes

## Principe

Le coût d'une carte se déduit de son budget de base (voir `gameplay/carte/budget.md`). Le budget vient de données de l'article sans lien avec sa popularité, donc le coût ne dépend pas de la popularité non plus. La popularité fixe la rareté (voir `gameplay/carte/rarete.md`), qui ajoute du budget sans changer le coût.

Comme dans Magic, une carte puissante coûte cher et une carte à 1 mana a sa place dans un deck.

## Mana

Un seul mana, générique. Toutes les cartes se paient avec le même mana, quelle que soit leur famille.

## Calcul

```
cout = arrondi(budget_base / points_par_mana)
```

`points_par_mana` vaut 2 pour commencer, à régler en partie de test.

Le coût se calcule sur le budget de base, avant le bonus de rareté. Deux cartes de même budget de base ont le même coût, même si l'une est mythique et l'autre commune.

Il n'y a pas de coût de base selon le type. Le coût minimum est 0. Il n'y a pas de coût maximum.
