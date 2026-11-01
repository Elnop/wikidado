# Coût des cartes

## Principe

Le coût d'une carte découle des mécaniques qui lui sont assignées. Le modèle choisit les mécaniques (voir `generation/pipeline.md`), puis le code calcule le coût à partir de ce choix. C'est la façon dont on conçoit une carte Magic : on part de ce que fait la carte et on en déduit ce qu'elle coûte.

Le coût ne dépend pas de la popularité de l'article. La popularité fixe la rareté (voir `gameplay/carte/rarete.md`) et, à travers elle, la puissance par rapport au coût (voir `gameplay/carte/stats.md`).

## Mana

Un seul mana, générique. Toutes les cartes se paient avec le même mana, quelle que soit leur famille.

## Calcul

Chaque mécanique du catalogue consomme des points de budget (`cout_budget`, voir `gameplay/mecanique.md`). Le coût de la carte est la somme de ces points, convertie en mana :

```
cout = arrondi(somme(cout_budget des mécaniques) / points_par_mana)
```

`points_par_mana` vaut 2 pour commencer, à régler en partie de test.

Il n'y a pas de coût de base selon le type. Le coût minimum est 0 : une carte sans mécanique est gratuite. Il n'y a pas de coût maximum.

Les stats prennent ensuite le budget du coût, multiplié par la rareté, moins ce que les mécaniques ont consommé (voir `gameplay/carte/stats.md`).

## Questions ouvertes

- Une carte sans mécanique coûte 0 et n'a qu'un point de stats (avant rareté). Les grosses créatures sans capacité n'existent donc pas. Faut-il des mécaniques qui ne font qu'ajouter des stats, pour permettre ces cartes ?
- Les paramètres d'une mécanique changent-ils son coût ? "+1 aux créatures Histoire" et "+1 à toutes vos créatures" ne valent pas la même chose.
- Comment garder une courbe de mana équilibrée si le coût n'est pas choisi directement ?
- Sans coût maximum, faut-il limiter le nombre de mécaniques par carte pour éviter des cartes injouables ?
