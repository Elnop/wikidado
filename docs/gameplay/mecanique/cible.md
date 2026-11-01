# Cibles et filtres

## Cibles

La cible dit sur qui porte l'effet. Chaque effet indique les cibles qu'il accepte (voir `gameplay/mecanique/effet.md`). La liste des cibles et leurs facteurs sont dans `config/mecanique/cible.json` : cette carte, une carte choisie, vous, l'adversaire (× 1), vos autres cartes et toutes les cartes adverses (× 3), toutes les cartes (× 2).

Avec ces facteurs, "Vos autres Créatures gagnent +1 en attaque" coûte 1 × 3 × 0,75 = 2,25, arrondi à 3.

## Filtres

Le filtre restreint la cible. Il est facultatif. Les filtres et leurs facteurs sont dans `config/mecanique/filtre.json` : un type (× 0,75), une famille (× 0,5, voir `gameplay/carte/famille.md`), ou une carte liée à l'article, remplie par le code (× 0,5).

Le filtre `carte-liee` vient des données de l'article, comme les conditions (voir `gameplay/mecanique/condition.md`).

Le coût maximum de `destruction` et `annexion` fait déjà partie de l'effet, ce n'est pas un filtre.
