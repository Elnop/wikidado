# wikidado

Jeu de cartes construit à partir des articles Wikipédia, avec un gameplay de duel inspiré de Magic: The Gathering. Projet de Leon et Dani. Pour l'instant le dépôt ne contient que de la documentation de conception, en français.

## Organisation

Toute la documentation est dans `docs/`. Le `README.md` à la racine sert d'index et doit être mis à jour quand on ajoute un fichier.

## Règle des idées

Toutes les idées du projet sont recensées dans `docs/Idees/index.md`, y compris celles qui ont été écartées.

- Ne jamais supprimer une idée, ni de l'index ni des documents de détail.
- Quand une idée est abandonnée, passer son statut à "écartée" avec la date et la raison dans l'index, puis déplacer son texte hors du document principal vers le dossier `ecartees/` de son domaine (par exemple `docs/Gameplay/ecartees/`), dans un fichier qui porte le nom du document d'origine (`cardcost.md` va dans `ecartees/cardcost.md`). Chaque idée y commence par "Écartée le JJ/MM/AAAA : raison". Mettre à jour la colonne "Détail" de l'index.
- Chaque nouvelle idée proposée, par Leon, Dani ou par Claude, est ajoutée à l'index avec le statut "à discuter".
- Une idée ne passe à "retenue" que si Leon ou Dani l'ont décidé. Une recommandation de Claude reste "à discuter".

## Git

Après chaque lot de modifications : commit en français et push sur `origin main`, sans redemander.
