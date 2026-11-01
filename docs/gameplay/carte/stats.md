# Stats des cartes

## Principe

Les stats reçoivent ce qui reste du budget effectif une fois les mécaniques payées (voir `gameplay/carte/budget.md`) :

```
budget_stats = budget_effectif - somme(cout_budget des mécaniques)
```

Seuls deux types ont des stats :

- les Créatures ont une attaque et une défense
- les Lieux ont seulement une défense : ils peuvent être attaqués à la place du joueur

Une Créature ou un Lieu sans mécanique met tout son budget dans ses stats. Les Événements, les Objets, les Savoirs et les Factions n'ont pas de stats : tout leur budget va dans les mécaniques.

Le budget effectif inclut le bonus de rareté, pas le coût. C'est le fonctionnement de Magic : les rares et mythiques y sont souvent plus efficaces que les communes au même coût. Une carte mythique à 4 électricité sera meilleure qu'une commune à 4 électricité, mais elle reste une carte qu'on ne joue pas au tour 1.

## Répartition attaque / défense

Cette répartition ne concerne que les Créatures. La répartition du budget de stats entre attaque et défense se décide en deux temps :

1. Le code applique une répartition par défaut selon le type et les sous-types de la carte (voir `gameplay/carte/type.md`) : un Militaire penche vers l'attaque, un Monument vers la défense. Ces règles sont définies par sous-type ou par groupe de sous-types.
2. Le modèle choisit la répartition finale à partir de ce point de départ, selon ce qu'il comprend du sujet. Il peut aussi donner à la carte des bonus d'attaque ou de défense pour l'orienter (voir `gameplay/mecanique/effet.md`).

Napoléon (Militaire, Homme politique, Monarque) partirait d'une répartition orientée attaque, que le modèle pourrait garder ou équilibrer.
