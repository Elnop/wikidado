# Effets

L'effet dit ce que fait la capacité. Son prix est donné pour la cible de référence : une seule carte, ou un joueur. La cible et le filtre le modifient ensuite (voir `gameplay/mecanique/cible.md`). `N` est un paramètre numérique choisi par le modèle dans les valeurs autorisées.

## Effets ponctuels

Pour les capacités déclenchées.

| id | texte | N | cout_effet | cibles possibles | indice |
|---|---|---|---|---|---|
| degats | "infligez {N} dégâts à {cible}" | 1 à 6 | N | Créatures, Lieux, adversaire | conflits, scandales, attaques, catastrophes, armes, critiques, pamphlets |
| soin | "gagnez {N} points de vie" | 2 à 8 | N / 2 | vous | personnalités aimées, fêtes, médecine |
| reparation | "effacez les dégâts de {cible}" | aucun | 1 | vos Créatures, vos Lieux | soins, reconstruction, maintenance |
| pioche | "piochez {N} cartes" | 1 à 3 | N × 2 | vous | savoir, encyclopédies, recherche, presse, bibliothèques |
| defausse | "l'adversaire défausse {N} cartes au hasard" | 1 à 2 | N × 3 | adversaire | censure, interdictions, autodafés, propagande |
| restauration | "reprenez en main {cible} de votre défausse" | aucun | 3 | une carte de votre défausse | restaurations, renaissances, retours |
| destruction | "détruisez {cible} de coût {N} ou moins" | 1 à 10 | N + 2 | toute carte en jeu | destructions, démolitions, assassinats, interdictions |
| renvoi | "renvoyez {cible} dans la main de son propriétaire" | aucun | 2 | toute carte en jeu | retraites, exils, rappels, annulations |
| ebauche | "{cible} perd toutes ses mécaniques" | aucun | 3 | toute carte en jeu | réformes, oublis, purges, réécritures |
| panne | "{cible} ne peut ni attaquer ni bloquer à son prochain tour" | aucun | 1 | Créatures | grèves, blocages, sièges, pannes |
| affaiblissement | "{cible} perd {N} en attaque jusqu'à la fin du tour" | 1 à 4 | N / 2 | Créatures | scandales, rumeurs, caricatures, désinformation |
| renfort | "{cible} gagne +{N}/+{N} jusqu'à la fin du tour" | 1 à 3 | N | Créatures | entraînements, renforts, harangues |
| surtension | "gagnez {N} électricité ce tour-ci" | 1 à 4 | N | vous | production d'énergie, inventions, révolutions industrielles |
| delestage | "l'adversaire a {N} électricité de moins à son prochain tour" | 1 à 3 | N × 2 | adversaire | coupures, sabotages, blocus, sanctions |
| annexion | "prenez le contrôle de {cible} de coût {N} ou moins" | 1 à 8 | N + 4 | Créatures adverses | annexions, conquêtes, débauchages, transferts |

"Au début de votre tour : gagnez 1 électricité" remplace l'ancienne centrale, au prix 1 × 3 = 3.

## Effets continus

Pour les capacités passives.

| id | texte | N | cout_effet | cibles possibles | indice |
|---|---|---|---|---|---|
| bonus-attaque | "{cible} gagne +{N} en attaque" | 1 à 3 | N | Créatures | sujets agressifs, chefs qui galvanisent |
| bonus-defense | "{cible} gagne +{N} en défense" | 1 à 3 | N | Créatures, Lieux | sujets solides, protecteurs, syndicats, alliances |
| mot-cle-donne | "{cible} a {mot-clé}" | aucun | prix du mot-clé | Créatures | écoles, doctrines, techniques, équipements |
| cout-reduit | "{cible} coûte 1 électricité de moins (minimum 1)" | aucun | 1 | vos cartes en main | enseignement, médias, popularisation d'un domaine |
| cout-augmente | "{cible} coûte 1 électricité de plus" | aucun | 1 | cartes adverses en main | embargos, taxes, réglementations, monopoles |
| protection | "{cible} ne peut pas être ciblée par les mécaniques adverses" | aucun | 3 | toute carte | sujets intouchables, sacrés |
| semi-protection | "les mécaniques adverses qui ciblent {cible} coûtent 2 électricité de plus" | aucun | 1 | toute carte | sujets surveillés, gardés |
| patrimoine | "{cible} ne peut pas être détruite par une mécanique, seulement au combat" | aucun | 3 | toute carte | patrimoine, monuments historiques, institutions anciennes |

Sur la carte elle-même, `bonus-attaque` et `bonus-defense` ne vont qu'aux types qui ont ces stats : Créature pour l'attaque, Créature et Lieu pour la défense. Ils remplacent les anciennes mécaniques robuste et offensif.
