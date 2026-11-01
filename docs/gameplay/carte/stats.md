# Stats des cartes

## Principe

Les stats (attaque et défense) reçoivent ce qui reste du budget effectif une fois les mécaniques payées (voir `gameplay/carte/budget.md`) :

```
budget_stats = budget_effectif - somme(cout_budget des mécaniques)
```

Une carte sans mécanique met tout son budget dans ses stats.

Le budget effectif inclut le bonus de rareté, pas le coût. C'est le fonctionnement de Magic : les rares et mythiques y sont souvent plus efficaces que les communes au même coût. Une Napoléon à 4 mana sera meilleure qu'une araignée inconnue à 4 mana, mais elle reste une carte à 4 mana qu'on ne joue pas au tour 1.

## Répartition attaque / défense

La répartition du budget de stats entre attaque et défense se décide en deux temps :

1. Le code applique une répartition par défaut selon le type et les sous-types de la carte (voir `gameplay/carte/type.md`) : un Militaire penche vers l'attaque, un Monument vers la défense. Ces règles sont définies par sous-type ou par groupe de sous-types.
2. Le modèle choisit la répartition finale à partir de ce point de départ, selon ce qu'il comprend du sujet. Il peut aussi assigner des mécaniques de stats pour orienter la carte (voir `gameplay/mecanique.md`).

Napoléon (Militaire, Homme politique, Monarque) partirait d'une répartition orientée attaque, que le modèle pourrait garder ou équilibrer.
