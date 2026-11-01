# wikidado

Jeu de cartes construit à partir des articles Wikipédia, avec un gameplay de duel inspiré de Magic: The Gathering. Projet de Leon et Dani.

## Organisation

```
docs/
  wikimaster/analyse.md        analyse de WikiMasters, le jeu existant le plus proche
  wikipedia/donnees.md         ce que Wikipédia et Wikidata mettent à disposition, mesuré sur de vrais articles
  gameplay/
    carte/
      type.md                  types de cartes
      budget.md                budget : source, bonus de rareté, dépense
      cout.md                  coût
      rarete.md                rareté
      stats.md                 budget de stats, attaque et défense
      famille.md               familles, utilisées pour les synergies
      illustration.md          image de la carte
    synergie/
      index.md                 ce qu'est une synergie, questions générales
      liens.md                 les articles se citent entre eux
      relations.md             relations typées de Wikidata
      epoques.md               dates de vie et d'événements
      categories.md            catégories Wikipédia
    deck/
      construction.md          construction de deck
    mecanique.md               catalogue fermé des mécaniques assignables
    tendance.md                bonus d'actualité
  generation/
    pipeline.md                partage entre code et petit modèle d'assignation
    article/
      selection.md             quels articles deviennent des cartes
  ecartees/                    idées écartées, rangées comme le reste de docs/
    gameplay/
      carte/budget.md
      carte/cout.md
      carte/famille.md
      carte/illustration.md
      carte/rarete.md
      carte/stats.md
      carte/type.md
      mecanique.md
      synergie/index.md
      duel.md
    generation/
      pipeline.md
      article/selection.md
```
