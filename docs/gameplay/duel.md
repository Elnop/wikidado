# Duel

Une partie oppose deux joueurs, chacun avec son deck. Le combat suit Magic (l'attaquant déclare, le défenseur bloque), le reste du tour suit plutôt Hearthstone : électricité automatique (voir `gameplay/electricite.md`) et aucune carte jouée pendant le tour adverse.

## Deck et début de partie

- Un deck contient 30 cartes, avec un seul exemplaire de chaque carte.
- Chaque joueur commence à 30 points de vie.
- Le premier joueur est tiré au sort. Les deux joueurs piochent 5 cartes.
- Chaque joueur peut ensuite, une seule fois, remettre dans son deck les cartes de sa main qu'il ne veut pas, et en repiocher autant.
- Le second joueur n'a pas d'autre compensation que la pioche dont le premier joueur est privé au tour 1.

## Victoire

Un joueur perd quand ses points de vie tombent à 0, ou quand il doit piocher alors que son deck est vide.

## Déroulé d'un tour

1. Début : la réserve d'électricité monte de 1 (jusqu'à 10) et se recharge entièrement. Le joueur pioche une carte, sauf le premier joueur à son premier tour.
2. Le joueur joue des cartes en payant leur coût en électricité.
3. Il peut ensuite attaquer. L'attaque termine sa phase de jeu : il ne pose plus de carte après.
4. Fin : les dégâts subis par les Créatures et les Lieux s'effacent.

Le joueur dont ce n'est pas le tour ne joue aucune carte. Il ne décide que de ses blocages.

Il n'y a pas de limite au nombre de cartes en jeu.

## Défausse

Les Événements joués et les cartes détruites vont dans la défausse de leur propriétaire. Elle est visible des deux joueurs. Des mécaniques peuvent s'en servir, par exemple pour ramener une carte ou compter les cartes détruites.

## Les cartes en jeu

- Créature : reste en jeu, attaque et bloque. Elle ne peut pas attaquer le tour où elle est jouée, sauf mécanique qui le permet.
- Lieu : reste en jeu, a une défense et peut être attaqué à la place du joueur. Il n'attaque pas et ne bloque pas.
- Événement : son effet s'applique quand il est joué, puis la carte part à la défausse.
- Objet : reste en jeu avec ses propres mécaniques, comme produire de l'électricité ou une capacité à activer. Certaines mécaniques l'attachent à une Créature, comme un équipement.
- Savoir : reste en jeu et agit sur le reste du jeu, sans capacité propre. Il donne des capacités aux autres cartes en jeu, renforce les cartes de son joueur, ou change les règles pour un joueur ou pour l'adversaire.
- Faction : reste en jeu et agit comme un Savoir, mais ses effets ne touchent que les Créatures qui lui sont affectées.

## Affectation à une Faction

Pendant son tour, avant d'attaquer, un joueur peut affecter une de ses Créatures en jeu à une de ses Factions en jeu. Il paie le coût d'affectation de la Faction en électricité. Ce coût est écrit sur la Faction.

- N'importe quelle Créature du joueur peut être affectée, au même prix, qu'elle soit liée ou non à la Faction dans Wikidata.
- Une Créature n'a qu'une Faction à la fois.
- Si la Faction quitte le jeu, ses Créatures restent en jeu sans affectation. On peut les affecter à une autre Faction en payant à nouveau.

Le calcul du coût d'affectation à partir de l'article reste à définir.

## Combat

1. L'attaquant déclare ses Créatures attaquantes, et pour chacune sa cible : le joueur adverse ou un de ses Lieux.
2. Le défenseur choisit ses bloqueurs parmi ses Créatures. Chaque bloqueur arrête un seul attaquant, mais plusieurs bloqueurs peuvent arrêter le même. Une Créature qui a attaqué à son propre tour peut bloquer au tour adverse suivant.
3. Les dégâts sont simultanés. Chaque bloqueur inflige son attaque à l'attaquant qu'il bloque. Un attaquant bloqué répartit son attaque entre ses bloqueurs comme il veut, et n'atteint pas sa cible même s'il lui reste des dégâts, sauf mécanique de piétinement. Une Créature non bloquée inflige son attaque à sa cible.
4. Une Créature ou un Lieu dont les dégâts subis atteignent sa défense est détruit. Comme les dégâts s'effacent en fin de tour, il faut détruire un Lieu en un seul tour.

Exemple : Napoléon (6/4) attaque, bloqué par Wellington (3/3) et Blücher (2/2). Napoléon prend 5 dégâts et meurt. Il répartit ses 6 dégâts, 3 sur chacun, et détruit les deux.
