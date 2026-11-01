# Mécaniques des Créatures

Format et règles communes dans `gameplay/mecanique/index.md`.

## Mécaniques de stats

Le catalogue contient des mécaniques qui ne font qu'ajouter des stats. Le reste du budget va déjà aux stats (voir `gameplay/carte/stats.md`), donc elles ne sont pas nécessaires pour faire une grosse carte sans capacité : elles servent au modèle à orienter une carte vers l'attaque ou la défense.

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
- params : lieu, rempli par le code avec `P19` (lieu de naissance) s'il existe comme carte Lieu
- condition : l'article a un `P19` qui correspond à une carte
- indice : s'applique automatiquement, le modèle n'a pas besoin de juger

### participant

- texte : "Quand vous jouez {evenement}, piochez une carte."
- types : Créature
- cout_budget : 1
- params : événement, rempli par le code avec `P1344` (a participé à)
- condition : l'article a un `P1344` qui correspond à une carte Événement
- indice : s'applique automatiquement
