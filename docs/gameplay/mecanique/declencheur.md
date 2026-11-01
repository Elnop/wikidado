# Déclencheurs

Le déclencheur dit quand une capacité déclenchée agit. Une capacité passive n'en a pas : elle agit tant que la carte est en jeu (voir `gameplay/mecanique/index.md`).

| id | texte | types | facteur | indice |
|---|---|---|---|---|
| a-la-une | "À la une" : quand la carte est jouée | tous | × 1 | effet marquant au moment où le sujet apparaît |
| posterite | "Postérité" : quand la carte est détruite | tous sauf Événement | - 1 au prix, minimum 1 | sujets dont l'héritage compte plus que la vie : martyrs, figures posthumes, ruines |
| debut-de-tour | "Au début de votre tour" | tous sauf Événement | × 3 | sujets qui produisent ou agissent en continu : usines, centrales, institutions |
| attaque | "Quand elle attaque" | Créature | × 2 | conquérants, sportifs offensifs, prédateurs |
| bloque | "Quand elle bloque" | Créature | × 1,5 | défenseurs, gardiens, résistants |
| subit-degats | "Quand elle subit des dégâts" | Créature, Lieu | × 1,5 | sujets qui se renforcent dans l'adversité, forteresses |
| arrivee-autre | "Quand une carte {filtre} arrive en jeu de votre côté" | tous sauf Événement | × 2 | chefs, mentors, lieux de rassemblement |
| destruction-autre | "Quand une carte {filtre} est détruite" | tous sauf Événement | × 2 | charognards, héritiers, mémoriaux |
| fin-de-tour | "À la fin de votre tour" | tous sauf Événement | × 3 (proposé) | sujets qui agissent après coup : bilans, récoltes, veilles |
| affectation | "Quand une Créature est affectée à cette Faction" | Faction | × 2 (proposé) | partis, clubs, mouvements qui recrutent |
| adversaire-joue | "Quand l'adversaire joue une carte {filtre}" | tous sauf Événement | × 2 (proposé) | contre-pouvoirs, rivaux, opposants, services de renseignement |

Les déclencheurs et leurs facteurs sont retenus pour l'instant, sauf ceux marqués "proposé".

Les déclencheurs `arrivee-autre`, `destruction-autre` et `adversaire-joue` prennent un filtre (voir `gameplay/mecanique/cible.md`), qui peut être une carte liée remplie par le code : "Quand vous jouez Bataille d'Austerlitz, piochez 1 carte."

`adversaire-joue` se déclenche pendant le tour adverse. C'est une réaction automatique : le joueur ne joue toujours aucune carte pendant le tour de l'adversaire (voir `gameplay/duel.md`).
