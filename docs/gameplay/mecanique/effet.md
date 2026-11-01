# Effets

L'effet dit ce que fait la capacité. Son prix est donné pour la cible de référence : une seule carte, ou un joueur. La cible et le filtre le modifient ensuite (voir `gameplay/mecanique/cible.md`). `n` est un paramètre numérique choisi par le modèle dans les valeurs autorisées.

La liste des effets est dans `config/mechanics/effect.json`. Chaque effet y a sa sorte (ponctuel ou continu), son texte, les valeurs de `n`, son prix, les cibles qu'il accepte, les types de cartes qu'il peut viser, la zone où il agit (jeu, main, défausse) et son indice. Le prix s'écrit `(per_n × n + flat + per_keyword_cost × prix du mot-clé) / divisor` : `N / 2` donne `per_n` 1 et `divisor` 2.

Les effets ponctuels (`"kind": "triggered"`) servent aux capacités déclenchées, les effets continus (`"kind": "static"`) aux capacités passives.

## Durée

Les effets qui ont `"has_duration": true` dans la config prennent une durée : "jusqu'à la fin du tour" (× 1) ou permanent (× 3). Les facteurs sont dans `config/mechanics/duration.json`.

Le prix d'un effet dans la config est celui de la version pour le tour. Exemples : renfort +1/+1 coûte 1 pour le tour et 3 pour toujours, ebauche coûte 1 pour le tour et 3 pour toujours, annexion d'une carte de coût 4 ou moins coûte 3 pour le tour et 8 pour toujours.

"Au début de votre tour : gagnez 1 électricité" remplace l'ancienne centrale, au prix 1 × 3 = 3.

## Équipement

L'effet `attach` ("attachez cet Objet à une de vos Créatures") est réservé aux Objets. Un Objet qui l'a est un Équipement :

- il a toujours un coût d'équipement, sous la forme d'une capacité activée : "{n} électricité : attachez cet Objet à une de vos Créatures". Son prix en budget est 4 - n, minimum 1 : Équipement 1 coûte 3, Équipement 2 coûte 2, Équipement 3 et plus coûte 1 (voir `gameplay/mecanique/declencheur.md`).
- certains s'équipent aussi en arrivant : "À la une : attachez cet Objet à une de vos Créatures", pour 1 de budget. Ils gardent quand même leur coût d'équipement, qui sert à les déplacer.
- ses effets visent la Créature équipée (cible `equipped`, voir `gameplay/mecanique/cible.md`).

Les règles de jeu de l'Équipement sont dans `gameplay/duel.md`.

Chaque effet indique aussi les types de cartes qui peuvent le porter (`types`). Un effet continu ne va jamais à un Événement.

## Stats de la carte elle-même

Sur la carte elle-même, `attack-bonus` et `defense-bonus` ne vont qu'aux types qui ont ces stats : Créature pour l'attaque, Créature et Lieu pour la défense. Ils remplacent les anciennes mécaniques robuste et offensif.
