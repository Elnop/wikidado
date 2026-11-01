# Effets

L'effet dit ce que fait la capacité. Son prix est donné pour la cible de référence : une seule carte, ou un joueur. La cible et le filtre le modifient ensuite (voir `gameplay/mecanique/cible.md`). `n` est un paramètre numérique choisi par le modèle dans les valeurs autorisées.

La liste des effets est dans `config/mecanique/effet.json`. Chaque effet y a sa sorte (ponctuel ou continu), son texte, les valeurs de `n`, son prix, les cibles qu'il accepte, les types de cartes qu'il peut viser, la zone où il agit (jeu, main, défausse), son indice et son statut. Le prix s'écrit `(par_n × n + fixe + par_prix_mot_cle × prix du mot-clé) / diviseur` : `N / 2` donne `par_n` 1 et `diviseur` 2.

Les effets ponctuels (`"sorte": "ponctuel"`) servent aux capacités déclenchées, les effets continus (`"sorte": "continu"`) aux capacités passives.

## Durée

Les effets qui ont `"duree": true` dans la config prennent une durée : "jusqu'à la fin du tour" (× 1) ou permanent (× 3). Les facteurs sont dans `config/mecanique/duree.json`.

Le prix d'un effet dans la config est celui de la version pour le tour. Exemples : renfort +1/+1 coûte 1 pour le tour et 3 pour toujours, ebauche coûte 1 pour le tour et 3 pour toujours, annexion d'une carte de coût 4 ou moins coûte 3 pour le tour et 8 pour toujours.

"Au début de votre tour : gagnez 1 électricité" remplace l'ancienne centrale, au prix 1 × 3 = 3.

## Stats de la carte elle-même

Sur la carte elle-même, `bonus-attaque` et `bonus-defense` ne vont qu'aux types qui ont ces stats : Créature pour l'attaque, Créature et Lieu pour la défense. Ils remplacent les anciennes mécaniques robuste et offensif.
