# wikidado

Jeu de cartes construit à partir des articles Wikipédia, avec un gameplay de duel inspiré de Magic: The Gathering. Projet de Leon et Dani.

## Organisation

- `docs/Wikimaster/` : analyse de WikiMasters, le jeu existant le plus proche
- `docs/Wikipedia/` : ce que Wikipédia et Wikidata mettent à disposition, mesuré sur de vrais articles
- `docs/Gameplay/` : pistes de game design
  - `cardtype.md` : types de cartes
  - `cardcost.md` : coût
  - `cardrarete.md` : rareté
  - `cardstats.md` : budget de stats, attaque et défense
  - `cardfamille.md` : familles (couleurs)
  - `cardsynergie.md` : synergies, avec un fichier par source (`synergie-liens.md`, `synergie-relations.md`, `synergie-epoques.md`, `synergie-categories.md`)
  - `mecaniques.md` : catalogue fermé des mécaniques assignables
  - `tendance.md` : bonus d'actualité
  - `deckbuilding.md` : construction de deck
  - `ecartees/` : idées écartées sur le gameplay
- `docs/Generation/` : génération automatique des cartes
  - `pipeline.md` : partage entre code et petit modèle d'assignation
  - `selection-articles.md` : quels articles deviennent des cartes
  - `ecartees/` : idées écartées sur la génération
