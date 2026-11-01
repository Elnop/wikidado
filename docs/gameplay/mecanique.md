# Catalogue des mécaniques

Liste fermée des mécaniques que le modèle peut assigner aux cartes (voir `generation/pipeline.md`). Les exemples ci-dessous servent à fixer le format. Aucune mécanique n'est validée.

## Format d'une mécanique

Chaque mécanique doit préciser :

- `id` : identifiant stable, utilisé dans le JSON du modèle
- `texte` : gabarit du texte affiché sur la carte, avec ses paramètres entre accolades
- `types` : types de cartes qui peuvent la recevoir
- `cout_budget` : points de budget qu'elle consomme dans le budget effectif de la carte (voir `gameplay/carte/budget.md`). Quand la mécanique a des paramètres, le coût est donné pour chaque valeur : "+1 aux créatures Histoire" coûte moins que "+1 à toutes vos créatures".
- `params` : paramètres possibles et leurs valeurs autorisées
- `condition` : données nécessaires dans la fiche de l'article (par exemple, la mécanique n'est proposée que si l'article a un lieu de naissance)
- `indice` : une phrase pour aider le modèle à choisir (à quel genre d'article elle va bien)

## Mécaniques de stats

Le catalogue contient des mécaniques qui ne font qu'ajouter des stats.

### robuste

- texte : aucun, la mécanique s'affiche seulement dans les stats de la carte
- types : Créature
- cout_budget : 2
- params : aucun
- effet : +2 en défense
- condition : aucune
- indice : sujets solides, durables, difficiles à abattre

## Exemples

### inspiration

- texte : "Les autres créatures {cible} que vous contrôlez gagnent +1 en attaque."
- types : Créature
- cout_budget : 2 si la cible est une famille, 4 si c'est toutes vos créatures
- params : cible parmi les familles du jeu, ou toutes
- condition : aucune
- indice : figures qui ont mené ou influencé d'autres personnes de leur domaine

### terre-natale

- texte : "Tant que vous contrôlez {lieu}, cette créature gagne +1/+1."
- types : Créature
- cout_budget : 1
- params : lieu, rempli par le code avec `P19` (lieu de naissance) s'il existe comme carte Terrain
- condition : l'article a un `P19` qui correspond à une carte
- indice : s'applique automatiquement, le modèle n'a pas besoin de juger

### participant

- texte : "Quand vous jouez {evenement}, piochez une carte."
- types : Créature
- cout_budget : 1
- params : événement, rempli par le code avec `P1344` (a participé à)
- condition : l'article a un `P1344` qui correspond à une carte Événement
- indice : s'applique automatiquement

Les mécaniques dont les paramètres viennent des données (terre-natale, participant) peuvent se passer du modèle. Le modèle sert surtout pour les mécaniques "de saveur" comme inspiration, où il faut comprendre le sujet.

## Données exploitables pour des capacités

- label "Article de qualité" ou "Bon article" : mot-clé de rareté ou capacité bonus (6 600 articles sur fr, assez rare pour être spécial)
- âge de l'article (création en 2003 pour Napoléon) : mot-clé "Ancien" ?
- coordonnées GPS : l'article est un lieu, voir `gameplay/carte/type.md` pour les terrains
- importance "maximum" dans un projet : carte iconique de sa famille

## À faire

- lister les mécaniques par type de carte
- fixer le coût en budget de chacune après des parties de test

## Questions ouvertes

- Le reste du budget va déjà aux stats (voir `gameplay/carte/stats.md`), donc une carte sans capacité a des stats sans mécanique de stats. Les mécaniques de stats servent-elles encore ?
