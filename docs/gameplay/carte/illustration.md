# Illustration des cartes

L'illustration d'une carte est l'image principale de son article, prise sur Wikimedia Commons (champ `thumbnail` du résumé REST ou `P18` sur Wikidata, voir `wikipedia/donnees.md`).

Un article sans image libre reste une carte. Il reçoit une illustration par défaut, choisie selon son type et sa grande famille (voir `gameplay/carte/type.md` et `gameplay/carte/famille.md`). Une carte a souvent plusieurs grandes familles : on prend celle de sa nature (`P31`), sans tenir compte des occupations. Napoléon, Humain, prend celle des humains. Avec 6 types et 6 grandes familles, il faut jusqu'à 36 illustrations par défaut.

Chaque image de Commons a sa propre licence, à vérifier fichier par fichier. L'auteur et la licence sont crédités dans la vue détaillée de la carte (voir `gameplay/carte/face.md`). L'image prend la plus grande partie de la face.
