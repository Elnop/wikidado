# wikidado

Jeu de cartes construit à partir des articles Wikipédia, avec un gameplay de duel inspiré de Magic: The Gathering. Projet de Leon et Dani. Pour l'instant le dépôt ne contient que de la documentation de conception, en français.

## Organisation

Toute la documentation est dans `docs/`. Le `README.md` à la racine sert d'index et doit être mis à jour quand on ajoute, renomme ou supprime un fichier.

## Nommage des fichiers de spec

- Dossiers et fichiers en minuscules, mots séparés par des tirets, sans accent : `carte-rarete.md`, pas `CarteRareté.md` ni `carte_rarete.md`.
- Noms en français, au singulier : `mecanique.md`, pas `mecaniques.md`.
- Un dossier par domaine directement sous `docs/` : `gameplay/`, `generation/`, `wikipedia/`, `wikimaster/`.
- Un concept par fichier. Le nom est `<objet>-<concept>.md` quand le concept décrit une partie d'un objet du jeu (`carte-cout.md`, `carte-stats.md`, `deck-construction.md`, `article-selection.md`). L'objet vient en premier pour que les fichiers d'un même objet soient groupés dans le dossier.
- Quand un concept a plusieurs déclinaisons, le fichier général porte le nom seul et chaque déclinaison a son fichier préfixé : `synergie.md`, puis `synergie-liens.md`, `synergie-epoques.md`...
- Un concept qui ne se rattache à aucun objet garde un nom simple : `tendance.md`, `pipeline.md`.
- Dans `ecartees/`, le fichier porte exactement le nom du document d'origine.
- Les renvois entre fichiers s'écrivent entre backticks, avec un chemin relatif au fichier courant ou à `docs/`.

## Règle des idées

Chaque domaine de `docs/` (gameplay, generation...) garde toutes ses idées, y compris celles qui ont été écartées.

- Ne jamais supprimer une idée.
- Les documents principaux du domaine sont des specs : ils décrivent le design actuel tel quel, sans historique (pas de section "Décision du...", pas de "on a décidé que", pas de renvoi vers les idées écartées). Les propositions pas encore tranchées y restent, présentées comme des pistes ou des questions ouvertes.
- Quand une idée est abandonnée, déplacer son texte hors du document principal vers le dossier `ecartees/` du domaine (par exemple `docs/gameplay/ecartees/`), dans un fichier qui porte le nom du document d'origine (`carte-cout.md` va dans `ecartees/carte-cout.md`). Chaque idée y commence par "Écartée le JJ/MM/AAAA : raison".
- Une idée n'est décidée ou écartée que si Leon ou Dani l'ont tranché. Une recommandation de Claude reste une proposition.

## Git

Après chaque lot de modifications : commit en français et push sur `origin main`, sans redemander.
