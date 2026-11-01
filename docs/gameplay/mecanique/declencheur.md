# Déclencheurs

Le déclencheur dit quand une capacité déclenchée agit. Une capacité passive n'en a pas : elle agit tant que la carte est en jeu (voir `gameplay/mecanique/index.md`).

La liste des déclencheurs, avec leur texte, les types qui peuvent les porter, leur facteur de prix et leur statut, est dans `config/mecanique/declencheur.json`. Les plus courants : À la une (quand la carte est jouée), Postérité (quand elle est détruite, retire 1 au prix au lieu de le multiplier), Au début de votre tour (× 3).

Les déclencheurs `arrivee-autre`, `destruction-autre` et `adversaire-joue` prennent un filtre (voir `gameplay/mecanique/cible.md`), qui peut être une carte liée remplie par le code : "Quand vous jouez Bataille d'Austerlitz, piochez 1 carte."

`adversaire-joue` se déclenche pendant le tour adverse. C'est une réaction automatique : le joueur ne joue toujours aucune carte pendant le tour de l'adversaire (voir `gameplay/duel.md`).
