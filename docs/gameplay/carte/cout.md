# Coût des cartes

## Principe

Le coût d'une carte découle des mécaniques qui lui sont assignées. Le modèle choisit les mécaniques (voir `generation/pipeline.md`), puis le code calcule le coût à partir de ce choix. C'est la façon dont on conçoit une carte Magic : on part de ce que fait la carte et on en déduit ce qu'elle coûte.

Le coût ne dépend pas de la popularité de l'article. La popularité fixe la rareté (voir `gameplay/carte/rarete.md`) et, à travers elle, la puissance par rapport au coût (voir `gameplay/carte/stats.md`).

Comme dans Magic, une carte puissante coûte cher et une carte à 1 mana a sa place dans un deck.

## Calcul

Proposition de départ :

```
cout = cout_de_base_du_type + somme(cout_mana des mécaniques assignées)
```

Chaque mécanique du catalogue a donc un `cout_mana` (voir `gameplay/mecanique.md`). Le coût de base du type permet à une carte sans mécanique d'avoir quand même un coût : une créature sans capacité coûterait 1 ou 2.

Le budget de stats se calcule ensuite à partir de ce coût et de la rareté (voir `gameplay/carte/stats.md`).

## Questions ouvertes

- Faut-il un coût de base par type, et combien ?
- Une mécanique ajoute-t-elle seulement du mana, ou consomme-t-elle aussi du budget de stats (`cout_budget`) ? Avec les deux, une capacité augmente le coût et donc le budget, puis en reprend une partie. Il faut vérifier que ça ne fait pas des cartes trop fortes ou trop faibles.
- Les paramètres d'une mécanique changent-ils son coût ? "+1 aux créatures Histoire" et "+1 à toutes vos créatures" ne valent pas la même chose.
- Comment garder une courbe de mana équilibrée si le coût n'est pas choisi directement ?
- Un seul type de mana générique, ou du mana coloré par famille (voir `gameplay/carte/famille.md`) ?
- Coût de 1 à 7 ou plus large ?
