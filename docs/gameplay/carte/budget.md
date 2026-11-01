# Budget des cartes

Le budget est la quantité de puissance d'une carte. Il fixe le coût de la carte (voir `gameplay/carte/cout.md`), puis il est dépensé en mécaniques (voir `gameplay/mecanique/index.md`) et en stats (voir `gameplay/carte/stats.md`).

## Budget de base

Le budget de base se calcule à partir de deux données de l'article qui n'ont rien à voir avec sa popularité : sa taille et son nombre de contributeurs. Les lectures et le nombre de langues n'y entrent pas.

```
budget_base = max(0, arrondi(log2(taille_ko) + log2(contributeurs + 1) / 2))
```

Le logarithme évite qu'un article énorme donne une carte démesurée. Un article de moins de 1 Ko donnerait un logarithme négatif, d'où le minimum à 0. Les coefficients sont à régler sur un vrai échantillon.

| Article | Taille | Contributeurs | Budget de base | Coût |
|---|---|---|---|---|
| Napoléon Ier | 260 Ko | 1 944 | 13 | 9 |
| Article moyen | 5 Ko | 10 | 4 | 3 |

Les données disponibles et leurs ordres de grandeur sont dans `wikipedia/donnees.md`.

## Bonus de rareté

La rareté (voir `gameplay/carte/rarete.md`) multiplie le budget sans changer le coût :

```
budget_effectif = arrondi(budget_base * multiplicateur_rarete)
```

L'arrondi se fait au plus proche : 13 × 1,25 = 16,25 donne 16, et 2 × 1,25 = 2,5 donne 3.

| Rareté | Multiplicateur |
|---|---|
| Commune | 1,0 |
| Peu commune | 1,1 |
| Rare | 1,25 |
| Mythique | 1,4 |

À coût égal, une carte populaire a donc plus de budget à dépenser qu'une carte obscure.

## Dépense du budget

1. Le modèle choisit des mécaniques dans le catalogue. Chacune consomme son `cout_budget`. La somme ne peut pas dépasser le budget effectif.
2. Ce qui reste du budget effectif va aux stats, pour les Créatures et les Lieux (voir `gameplay/carte/stats.md`). Ils gardent toujours au moins 1 point pour la défense. Pour les Événements, les Objets, les Savoirs et les Factions, qui n'ont pas de stats, tout le budget doit être dépensé en mécaniques.

Une Faction a aussi un coût d'affectation (voir `gameplay/duel.md`). Il part d'une valeur de départ élevée, et le modèle peut dépenser du budget pour le baisser, jusqu'à 0. Une Faction puissante a donc des effets forts ou une affectation bon marché, rarement les deux. La valeur de départ et le prix en budget d'une électricité retirée sont à régler en partie de test.

Il n'y a pas de nombre maximum de mécaniques par carte, ni de synergies : seul le budget limite. Un Lieu doit avoir au moins une capacité : sans elle, il ne bloque pas, n'attaque pas, et l'adversaire n'a aucune raison de le viser.

## Questions ouvertes

- Une carte à budget effectif 0 (article de moins de 1 Ko presque sans contributeur) n'a rien à dépenser : un Événement, un Objet, un Savoir ou une Faction serait vide, et une Créature ne pourrait pas avoir sa défense de 1. Piste : un budget de base minimum de 1.
