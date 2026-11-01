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

Le prix de À la une, Postérité et Au début de votre tour a été retenu pour l'instant. Les autres facteurs sont des propositions.

Les déclencheurs `arrivee-autre` et `destruction-autre` prennent un filtre (voir `gameplay/mecanique/cible.md`), qui peut être une carte liée remplie par le code : "Quand vous jouez Bataille d'Austerlitz, piochez 1 carte."
