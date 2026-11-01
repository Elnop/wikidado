# Duel

Une partie oppose deux joueurs, chacun avec son deck. Le combat suit Magic (l'attaquant déclare, le défenseur bloque), le reste du tour suit plutôt Hearthstone : électricité automatique (voir `gameplay/electricite.md`) et aucune carte jouée pendant le tour adverse.

## Deck et début de partie

- Un deck contient 30 cartes, avec un seul exemplaire de chaque carte.
- Chaque joueur commence à 30 points de vie.
- Le premier joueur est tiré au sort. Les deux joueurs piochent 5 cartes.

## Victoire

Un joueur perd quand ses points de vie tombent à 0, ou quand il doit piocher alors que son deck est vide.

## Déroulé d'un tour

1. Début : la réserve d'électricité monte de 1 (jusqu'à 10) et se recharge entièrement. Le joueur pioche une carte, sauf le premier joueur à son premier tour.
2. Le joueur joue des cartes en payant leur coût en électricité, et peut attaquer une fois.
3. Fin : les dégâts subis par les Créatures et les Lieux s'effacent.

Le joueur dont ce n'est pas le tour ne joue aucune carte. Il ne décide que de ses blocages.

## Les cartes en jeu

- Créature : reste en jeu, attaque et bloque. Elle ne peut pas attaquer le tour où elle est jouée, sauf mécanique qui le permet.
- Lieu : reste en jeu, a une défense et peut être attaqué à la place du joueur. Il n'attaque pas et ne bloque pas.
- Événement : son effet s'applique quand il est joué, puis la carte part à la défausse.
- Objet : reste en jeu avec ses propres mécaniques, comme produire de l'électricité ou une capacité à activer. Certaines mécaniques l'attachent à une Créature, comme un équipement.
- Savoir : reste en jeu et agit sur le reste du jeu, sans capacité propre. Il donne des capacités aux autres cartes en jeu, renforce les cartes de son joueur, ou change les règles pour un joueur ou pour l'adversaire.

## Combat

1. L'attaquant déclare ses Créatures attaquantes, et pour chacune sa cible : le joueur adverse ou un de ses Lieux.
2. Le défenseur choisit ses bloqueurs parmi ses Créatures. Une Créature qui a attaqué à son propre tour peut bloquer au tour adverse suivant.
3. Les dégâts sont simultanés. Une Créature bloquée et son bloqueur s'infligent chacun leur attaque. Une Créature non bloquée inflige son attaque à sa cible.
4. Une Créature ou un Lieu dont les dégâts subis atteignent sa défense est détruit. Comme les dégâts s'effacent en fin de tour, il faut détruire un Lieu en un seul tour.

## Questions ouvertes

- Plusieurs Créatures peuvent-elles bloquer le même attaquant, et qui répartit alors les dégâts ?
- Une Créature bloquée par un adversaire plus faible inflige-t-elle le surplus de dégâts à sa cible (piétinement), ou seulement avec une mécanique ?
- Peut-on rejouer des cartes après l'attaque, ou l'attaque termine-t-elle le tour ?
- Faut-il une limite de cartes en jeu par joueur ?
- Un joueur peut-il repiocher une main de départ qui ne lui convient pas (mulligan) ?
- Le second joueur reçoit-il une compensation en plus de la pioche du tour 1 ?
