# Déclencheurs

Le déclencheur dit quand une capacité déclenchée agit. Une capacité passive n'en a pas : elle agit tant que la carte est en jeu (voir `gameplay/mecanique/index.md`).

La liste des déclencheurs, avec leur texte, les types qui peuvent les porter et leur facteur de prix, est dans `config/mechanics/trigger.json`. Les plus courants : À la une (quand la carte est jouée), Postérité (quand elle est détruite, retire 1 au prix au lieu de le multiplier), Au début de votre tour (× 3).

Les déclencheurs `other-enters`, `other-destroyed` et `opponent-plays` prennent un filtre (voir `gameplay/mecanique/cible.md`), qui peut être une carte liée remplie par le code : "Quand vous jouez Bataille d'Austerlitz, piochez 1 carte."

`opponent-plays` se déclenche pendant le tour adverse. C'est une réaction automatique : le joueur ne joue toujours aucune carte pendant le tour de l'adversaire (voir `gameplay/duel.md`).

## Capacités activées

Le déclencheur `activated` s'écrit "{n} électricité :". Le joueur paie n électricité pendant son tour, avant d'attaquer, pour que l'effet ait lieu. Chaque capacité activée ne s'utilise qu'une fois par tour. Toutes les cartes qui restent en jeu peuvent en avoir.

Son facteur dépend de n : 4 - n, minimum 1. "1 électricité : infligez 1 dégât à une carte adverse" coûte 1 × 3 = 3 de budget, comme "Au début de votre tour". "2 électricité : piochez 1 carte" coûte 2 × 2 = 4. Dans la config, ce calcul s'écrit `factor + factor_per_n × n`, avec `factor_minimum` comme plancher.
