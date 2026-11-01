# Cibles et filtres

## Cibles

La cible dit sur qui porte l'effet. Chaque effet indique les cibles qu'il accepte (voir `gameplay/mecanique/effet.md`).

| id | texte | facteur |
|---|---|---|
| cette-carte | "cette carte" | × 1 |
| une | "une carte" choisie par le joueur quand la capacité agit | × 1 |
| vous | "vous" | × 1 |
| adversaire | "l'adversaire" | × 1 |
| vos-autres | "vos autres cartes" | × 3 |
| toutes-adverses | "toutes les cartes adverses" | × 3 |
| toutes | "toutes les cartes", des deux côtés | × 2 |

Avec ces facteurs, "Vos autres Créatures gagnent +1 en attaque" coûte 1 × 3 × 0,75 = 2,25, arrondi à 3.

## Filtres

Le filtre restreint la cible. Il est facultatif.

| id | texte | facteur | rempli par |
|---|---|---|---|
| type | un des 6 types : "Créature", "Lieu"... | × 0,75 | le modèle |
| famille | une famille (voir `gameplay/carte/famille.md`) : "Militaire", "Sport"... | × 0,5 | le modèle |
| carte-liee | une carte précise, liée à l'article : "Ajaccio", "Joséphine de Beauharnais" | × 0,5 | le code |

Le filtre `carte-liee` vient des données de l'article, comme les conditions (voir `gameplay/mecanique/condition.md`).

Le coût maximum de `destruction` et `annexion` fait déjà partie de l'effet, ce n'est pas un filtre.
