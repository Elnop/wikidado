# Catalogue des mécaniques

Liste fermée des mécaniques que le modèle peut assigner aux cartes (voir `Generation/pipeline.md`). Les exemples ci-dessous servent à fixer le format. Aucune mécanique n'est validée.

## Format d'une mécanique

Chaque mécanique doit préciser :

- `id` : identifiant stable, utilisé dans le JSON du modèle
- `texte` : gabarit du texte affiché sur la carte, avec ses paramètres entre accolades
- `types` : types de cartes qui peuvent la recevoir
- `cout_budget` : points de budget de stats qu'elle consomme
- `params` : paramètres possibles et leurs valeurs autorisées
- `condition` : données nécessaires dans la fiche de l'article (par exemple, la mécanique n'est proposée que si l'article a un lieu de naissance)
- `indice` : une phrase pour aider le modèle à choisir (à quel genre d'article elle va bien)

## Exemples

### inspiration

- texte : "Les autres créatures {famille} que vous contrôlez gagnent +1 en attaque."
- types : Créature
- cout_budget : 2
- params : famille parmi les familles du jeu
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

## À faire

- lister les mécaniques par type de carte
- fixer le coût en budget de chacune après des parties de test
