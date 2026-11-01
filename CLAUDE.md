# wikidado

Jeu de cartes construit à partir des articles Wikipédia, avec un gameplay de duel inspiré de Magic: The Gathering. Projet de Leon et Dani. Pour l'instant le dépôt ne contient que de la documentation de conception, en français.

## Organisation

Toute la documentation est dans `docs/`. Le `README.md` à la racine sert d'index et doit être mis à jour quand on ajoute un fichier.

## Règle des idées

Chaque domaine de `docs/` (Gameplay, Generation...) garde toutes ses idées, y compris celles qui ont été écartées.

- Ne jamais supprimer une idée.
- Les documents principaux du domaine sont des specs : ils décrivent le design actuel tel quel, sans historique (pas de section "Décision du...", pas de "on a décidé que", pas de renvoi vers les idées écartées). Les propositions pas encore tranchées y restent, présentées comme des pistes ou des questions ouvertes.
- Quand une idée est abandonnée, déplacer son texte hors du document principal vers le dossier `ecartees/` du domaine (par exemple `docs/Gameplay/ecartees/`), dans un fichier qui porte le nom du document d'origine (`cardcost.md` va dans `ecartees/cardcost.md`). Chaque idée y commence par "Écartée le JJ/MM/AAAA : raison".
- Une idée n'est décidée ou écartée que si Leon ou Dani l'ont tranché. Une recommandation de Claude reste une proposition.

## Git

Après chaque lot de modifications : commit en français et push sur `origin main`, sans redemander.
