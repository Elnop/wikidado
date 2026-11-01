# Stats des cartes

## Principe

Les stats (attaque et défense) reçoivent ce qui reste du budget effectif une fois les mécaniques payées (voir `gameplay/carte/budget.md`) :

```
budget_stats = budget_effectif - somme(cout_budget des mécaniques)
```

Une carte sans mécanique met tout son budget dans ses stats.

Le budget effectif inclut le bonus de rareté, pas le coût. C'est le fonctionnement de Magic : les rares et mythiques y sont souvent plus efficaces que les communes au même coût. Une Napoléon à 4 mana sera meilleure qu'une araignée inconnue à 4 mana, mais elle reste une carte à 4 mana qu'on ne joue pas au tour 1.

## Répartition attaque / défense

Les données de l'article décident de la répartition du budget de stats :

- attaque : taille de l'article (ce que le sujet "a à dire")
- défense : nombre de contributeurs (un article défendu par beaucoup de monde est solide)

On compare l'article à la médiane des articles de même coût. Un article plus long que la médiane penche vers l'attaque, un article avec plus de contributeurs penche vers la défense. Pour Napoléon, 260 Ko et 1 944 contributeurs : les deux sont très hauts, donc carte équilibrée. Un article court mais très contributé donnerait un mur défensif.
