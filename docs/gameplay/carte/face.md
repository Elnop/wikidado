# Face de la carte

Une carte peut avoir un nombre illimité de mécaniques, donc leur texte ne tient pas sur la face, contrairement à Magic. La face montre peu de choses, et l'image prend le plus de place.

## Ce qui est sur la face

- le nom de l'article
- le type principal : Lieu, Créature, Événement, Objet, Savoir ou Faction (voir `gameplay/carte/type.md`). Les sous-types n'y sont pas.
- le coût en électricité (voir `gameplay/carte/cout.md`)
- pour une Faction, le coût d'affectation en électricité (voir `gameplay/duel.md`)
- les stats : attaque et défense pour une Créature, défense pour un Lieu (voir `gameplay/carte/stats.md`)
- l'illustration (voir `gameplay/carte/illustration.md`), en grand
- un court texte de lore : la première phrase du résumé de l'article Wikipédia. Le code retire les transcriptions phonétiques entre crochets et les parenthèses de prononciation ("La tour Eiffel [tuʁɛfɛl] est..." devient "La tour Eiffel est..."), le reste de la phrase est gardé tel quel.

La rareté n'est pas écrite : elle se voit au style de la carte (cadre, couleurs). Voir `gameplay/carte/rarete.md`.

Exemple de lore, Napoléon Ier : "Napoléon Bonaparte, né le 15 août 1769 à Ajaccio en Corse et mort le 5 mai 1821 à Longwood sur l'île de Sainte-Hélène, est un militaire et homme d'État français." Sur les cinq cartes de la planche d'exemples, la première phrase fait entre 79 et 200 caractères.

## Vue détaillée

Un clic ou un survol sur la carte ouvre une vue détaillée qui montre tout le reste :

- les mécaniques, avec leur texte complet (voir `gameplay/mecanique/index.md`)
- les sous-types et les familles (voir `gameplay/carte/famille.md`)
- les crédits : lien vers l'article et ses auteurs (CC BY-SA 4.0), auteur et licence de l'image
