# wikidado

Jeu de cartes construit à partir des articles Wikipédia, avec un gameplay de duel inspiré de Magic: The Gathering. Projet de Leon et Dani. Pour l'instant le dépôt ne contient que de la documentation de conception, en français.

## Organisation

Toute la documentation est dans `docs/`. Le `README.md` à la racine sert d'index et doit être mis à jour quand on ajoute, renomme ou supprime un fichier.

## Nommage et rangement des fichiers de spec

- Dossiers et fichiers en minuscules, mots séparés par des tirets, sans accent : `rarete.md`, pas `Rareté.md` ni `rarete_detail.md`.
- Noms en français, au singulier : `mecanique.md`, pas `mecaniques.md`.
- Un dossier par domaine directement sous `docs/` : `gameplay/`, `generation/`, `wikipedia/`, `wikimaster/`.
- Dans un domaine, un dossier par objet du jeu (`carte/`, `synergie/`, `article/`), et un fichier par concept de cet objet : `gameplay/carte/cout.md`, `gameplay/carte/stats.md`. Le nom du fichier ne répète pas celui du dossier.
- Le fichier général d'un dossier, quand il en faut un, s'appelle `index.md` (`gameplay/synergie/index.md`).
- Un concept qui ne se rattache à aucun objet reste à la racine du domaine, avec un nom simple : `gameplay/electricite.md`, `generation/pipeline.md`.
- Les idées écartées vont dans `docs/ecartees/`, qui reproduit l'arborescence de `docs/` : `gameplay/carte/cout.md` a ses idées écartées dans `ecartees/gameplay/carte/cout.md`.
- Les renvois entre fichiers s'écrivent entre backticks, avec le chemin depuis `docs/` : `gameplay/carte/rarete.md`.

## Règle des idées

On garde toutes les idées, y compris celles qui ont été écartées.

- Ne jamais supprimer une idée.
- Les documents principaux du domaine sont des specs : ils décrivent le design actuel tel quel, sans historique (pas de section "Décision du...", pas de "on a décidé que", pas de renvoi vers les idées écartées). Les propositions pas encore tranchées y restent, présentées comme des pistes ou des questions ouvertes.
- Quand une idée est abandonnée, déplacer son texte hors du document principal vers `docs/ecartees/`, au même chemin que le document d'origine (voir la règle de rangement ci-dessus). Chaque idée y commence par "Écartée le JJ/MM/AAAA : raison".
- Une idée n'est décidée ou écartée que si Leon ou Dani l'ont tranché. Une recommandation de Claude reste une proposition.

## Travaux différés

Tout sujet mis de côté ("on verra après la première version", point pas encore tranché qu'on remet à plus tard) est noté dans `docs/differe.md`, avec la date, l'échéance et la spec concernée. Il n'apparaît pas dans la spec elle-même. Quand le sujet est traité, on le retire de `docs/differe.md` et on reporte le résultat dans la spec.

## Questions

Claude pose toutes ses questions à Leon avec l'outil de questions interactif de Claude Code (AskUserQuestion), jamais en texte libre dans sa réponse. Chaque réponse obtenue est reportée dans les specs concernées : la spec décrit le choix fait, et les options rejetées vont dans `docs/ecartees/`.

## Git

Après chaque lot de modifications : commit en français et push sur `origin main`, sans redemander.
