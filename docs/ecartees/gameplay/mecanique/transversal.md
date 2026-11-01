# Mécaniques ouvertes à tous les types

Écartée le 01/11/2026 : les capacités se composent de briques (déclencheur, effet, cible, filtre, condition) au lieu d'une liste de mécaniques fixes. Voir `gameplay/mecanique/index.md`. Les effets, les noms et les indices ci-dessous ont été repris dans les briques.

Format et règles communes dans `gameplay/mecanique/index.md`. Premier jet : les noms, les textes et les coûts sont des propositions, rien n'est validé.

Les coûts suivent l'étalon proposé dans `gameplay/mecanique/index.md` : 1 point de budget vaut 1 point de stat. `N` désigne un paramètre numérique, et le coût est donné en fonction de `N`. Une mécanique va à tous les types sauf mention contraire.

## Moments

Beaucoup de mécaniques sont des effets ponctuels. Elles prennent un paramètre `moment` qui dit quand l'effet a lieu :

| Moment | Quand | Types | Coût |
|---|---|---|---|
| À la une | quand la carte est jouée | tous | coût de base |
| Postérité | quand la carte est détruite | tous sauf Événement | coût de base - 1, minimum 1 |
| Chaque tour | au début de chacun de vos tours, tant que la carte est en jeu | tous sauf Événement | coût de base × 3 |

Pour un Événement, À la une est le seul moment possible : c'est son effet quand on le joue.

## Dégâts et soin

| id | texte | params | cout_budget | indice |
|---|---|---|---|---|
| polemique | "{moment} : infligez {N} dégâts à une Créature ou un Lieu." | moment, N de 1 à 6 | N | conflits, scandales, attaques, catastrophes, armes |
| requisitoire | "{moment} : infligez {N} dégâts à l'adversaire." | moment, N de 1 à 5 | N | critiques, pamphlets, campagnes contre quelqu'un |
| salve | "{moment} : infligez {N} dégâts à chaque Créature adverse." | moment, N de 1 à 3 | N × 3 | bombardements, épidémies, catastrophes de grande ampleur |
| popularite | "{moment} : gagnez {N} points de vie." | moment, N de 2 à 8 | N / 2, arrondi au supérieur | personnalités aimées, fêtes, médecine, soins |
| reparation | "{moment} : effacez les dégâts d'une de vos Créatures ou d'un de vos Lieux." | moment | 1 | soins, reconstruction, maintenance |

## Pioche et défausse

| id | texte | params | cout_budget | indice |
|---|---|---|---|---|
| consultation | "{moment} : piochez {N} cartes." | moment, N de 1 à 3 | N × 2 | savoir, encyclopédies, recherche, presse, bibliothèques |
| censure | "{moment} : l'adversaire défausse {N} cartes au hasard." | moment, N de 1 à 2 | N × 3 | censure, interdictions, autodafés, propagande |
| restauration | "{moment} : reprenez en main une carte {cible} de votre défausse." | moment, cible parmi les types ou les familles, ou toutes | 3, 2 si la cible est un type ou une famille | restaurations, renaissances, retours, résurrections |
| memoire | "Cette carte gagne +1/+1 pour chaque carte {cible} de votre défausse, jusqu'à +{N}/+{N}." | cible, N de 2 à 5 | N | commémorations, histoire, héritage, deuil |

memoire ne va qu'aux cartes qui ont des stats : Créatures et Lieux. Un Lieu n'utilise que la défense.

## Destruction et contrôle

| id | texte | params | cout_budget | indice |
|---|---|---|---|---|
| suppression | "{moment} : détruisez une carte adverse {cible} de coût {N} ou moins." | moment, cible parmi Créature, Lieu, Objet, Savoir, Faction, N de 1 à 10 | N + 2 | destructions, démolitions, assassinats, interdictions |
| mise-en-brouillon | "{moment} : renvoyez une carte en jeu dans la main de son propriétaire." | moment | 2 | retraites, exils, rappels, annulations |
| ebauche | "{moment} : une carte en jeu perd toutes ses mécaniques." | moment | 3 | réformes, oublis, purges, réécritures |
| panne | "{moment} : une Créature adverse ne peut ni attaquer ni bloquer à son prochain tour." | moment | 1 | grèves, blocages, sièges, pannes, embargos |
| discredit | "{moment} : une Créature adverse perd {N} en attaque jusqu'à la fin du tour." | moment, N de 1 à 4 | N / 2, arrondi au supérieur | scandales, rumeurs, caricatures, désinformation |
| annexion | "{moment} : prenez le contrôle d'une Créature adverse de coût {N} ou moins." | moment, N de 1 à 8 | N + 4 | annexions, conquêtes, débauchages, transferts |

## Bonus aux autres cartes

| id | texte | params | cout_budget | indice |
|---|---|---|---|---|
| inspiration | "Les autres Créatures {cible} que vous contrôlez gagnent +1 en attaque." | cible parmi les familles du jeu, ou toutes | 2 si la cible est une famille, 4 si c'est toutes vos Créatures | figures qui ont mené ou influencé d'autres personnes de leur domaine |
| solidarite | "Les autres Créatures {cible} que vous contrôlez gagnent +1 en défense." | cible parmi les familles du jeu, ou toutes | 2 si la cible est une famille, 4 si c'est toutes vos Créatures | syndicats, alliances, protections collectives |
| renfort | "{moment} : une Créature gagne +{N}/+{N} jusqu'à la fin du tour." | moment, N de 1 à 3 | N | entraînements, renforts, dopage, harangues |
| transmission | "Les Créatures {cible} que vous contrôlez ont {mot-cle}." | cible, mot-clé parmi ceux des Créatures (voir `gameplay/mecanique/creature.md`) | coût du mot-clé × 2 si la cible est une famille, × 4 si c'est toutes vos Créatures | écoles, doctrines, techniques, équipements partagés |

## Électricité et coûts

| id | texte | params | cout_budget | indice |
|---|---|---|---|---|
| centrale | "Au début de votre tour, gagnez {N} électricité." | N de 1 à 3 | N × 3 | production d'énergie : centrales, barrages, machine à vapeur, ingénieurs, découvertes scientifiques |
| surtension | "{moment} : gagnez {N} électricité ce tour-ci." | moment, N de 1 à 4 | N | inventions soudaines, révolutions industrielles, coups d'éclat |
| delestage | "{moment} : l'adversaire a {N} électricité de moins à son prochain tour." | moment, N de 1 à 3 | N × 2 | coupures, sabotages, blocus, sanctions |
| vulgarisation | "Vos cartes {cible} coûtent 1 électricité de moins (minimum 1)." | cible parmi les types ou les familles | 3 | enseignement, médias, popularisation d'un domaine |
| embargo | "Les cartes adverses {cible} coûtent 1 électricité de plus." | cible parmi les types ou les familles, ou toutes | 2 si la cible est un type ou une famille, 5 si c'est toutes | embargos, taxes, réglementations, monopoles |

## Protection

| id | texte | params | cout_budget | indice |
|---|---|---|---|---|
| protege | "Cette carte ne peut pas être ciblée par les mécaniques adverses." | aucun | 3 | sujets intouchables, sacrés, très protégés |
| semi-protege | "Les mécaniques adverses qui ciblent cette carte coûtent 2 électricité de plus." | aucun | 1 | sujets surveillés, gardés |
| patrimoine | "Cette carte ne peut pas être détruite par une mécanique. Elle peut être détruite au combat." | aucun | 3 | patrimoine, monuments historiques, institutions anciennes |

## Synergies tirées des données

Ces mécaniques sont remplies par le code (voir `gameplay/synergie/index.md`). Le modèle n'a pas à juger.

| id | texte | params | cout_budget | condition |
|---|---|---|---|---|
| reference | "Tant que vous contrôlez {carte}, cette carte {effet}." | carte, remplie par le code avec un article cité ; effet parmi +1/+1, coûte 1 de moins, pioche au début du tour | 1 | l'article cite un autre article qui existe comme carte (voir `gameplay/synergie/liens.md`) |
| alliance | "Tant que vous contrôlez {carte}, cette carte et {carte} {effet}." | comme reference, l'effet s'applique aux deux cartes | 2 | les deux articles se citent l'un l'autre |
| contemporain | "{moment} : si vous contrôlez une carte de la même époque, {effet}." | moment, effet parmi pioche, +1/+1, 1 électricité | 1 | l'article a des dates (voir `gameplay/synergie/epoques.md`) |
