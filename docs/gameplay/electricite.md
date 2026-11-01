# Électricité

La ressource du jeu est l'électricité. Elle sert à payer le coût des cartes (voir `gameplay/carte/cout.md`).

Chaque joueur reçoit de l'électricité à chaque tour, comme le mana dans Hearthstone : les joueurs n'ont pas besoin de poser des cartes pour en avoir. La réserve vaut 1 au premier tour et monte de 1 par tour, jusqu'à 10. Elle se recharge entièrement au début de chaque tour.

Le coût d'une carte n'a pas de maximum (voir `gameplay/carte/cout.md`). Une carte qui coûte plus de 10 ne peut se jouer qu'avec l'électricité en plus produite par des Lieux.

Certaines cartes produisent de l'électricité en plus, quel que soit leur type : un Lieu (une centrale, un barrage), un Objet (la machine à vapeur), une Créature (un ingénieur), un Événement (une découverte). La production d'électricité est une mécanique du catalogue, qui consomme du budget comme les autres (voir `gameplay/mecanique/transversal.md`).
