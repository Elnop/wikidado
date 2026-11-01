# wikidado

Jeu de cartes construit à partir des articles Wikipédia, avec un gameplay de duel inspiré de Magic: The Gathering. Projet de Leon et Dani.

## Organisation

- `docs/wikimaster/` : analyse de WikiMasters, le jeu existant le plus proche
- `docs/wikipedia/` : ce que Wikipédia et Wikidata mettent à disposition, mesuré sur de vrais articles
- `docs/gameplay/` : pistes de game design
  - `carte-type.md` : types de cartes
  - `carte-cout.md` : coût
  - `carte-rarete.md` : rareté
  - `carte-stats.md` : budget de stats, attaque et défense
  - `carte-famille.md` : familles (couleurs)
  - `synergie.md` : synergies, avec un fichier par source (`synergie-liens.md`, `synergie-relations.md`, `synergie-epoques.md`, `synergie-categories.md`)
  - `mecanique.md` : catalogue fermé des mécaniques assignables
  - `tendance.md` : bonus d'actualité
  - `deck-construction.md` : construction de deck
  - `ecartees/` : idées écartées sur le gameplay
- `docs/generation/` : génération automatique des cartes
  - `pipeline.md` : partage entre code et petit modèle d'assignation
  - `article-selection.md` : quels articles deviennent des cartes
  - `ecartees/` : idées écartées sur la génération
