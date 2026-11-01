# Stats des cartes

## Principe

À coût égal, une carte populaire est plus forte qu'une carte obscure. La popularité passe par la rareté (voir `carte-rarete.md`), qui multiplie le budget de stats. Le coût lui-même est décrit dans `carte-cout.md`.

C'est le fonctionnement de Magic : les rares et mythiques y sont souvent plus efficaces que les communes au même coût. Une Napoléon à 4 mana sera meilleure qu'une araignée inconnue à 4 mana, mais elle reste une carte à 4 mana qu'on ne joue pas au tour 1.

## Budget de stats

Comme dans Magic où une créature à N mana a environ N+1 en force + endurance sans capacité, chaque coût donne un budget de base, multiplié selon la rareté :

```
budget = (2 * cout + 1) * multiplicateur_rarete
```

Multiplicateurs de départ, à régler en partie de test :

| Rareté | Multiplicateur |
|---|---|
| Commune | 1,0 |
| Peu commune | 1,1 |
| Rare | 1,25 |
| Mythique | 1,4 |

Une commune à 3 a 7 points à répartir, une mythique à 3 en a environ 10. Une capacité coûte des points de budget (voir `mecanique.md`).

## Répartition attaque / défense

Les données de l'article décident de la répartition du budget :

- attaque : taille de l'article (ce que le sujet "a à dire")
- défense : nombre de contributeurs (un article défendu par beaucoup de monde est solide)

On compare l'article à la médiane des articles de même coût. Un article plus long que la médiane penche vers l'attaque, un article avec plus de contributeurs penche vers la défense. Pour Napoléon, 260 Ko et 1 944 contributeurs : les deux sont très hauts, donc carte équilibrée. Un article court mais très contributé donnerait un mur défensif.
