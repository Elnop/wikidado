# wikidado

Jeu de cartes construit à partir des articles Wikipédia, avec un gameplay de duel inspiré de Magic: The Gathering. Projet de Leon et Dani.

## Planche d'exemples

Cinq cartes construites à partir de vrais articles, avec le détail de chaque valeur : https://claude.ai/artifact/AEf324h7RW7noueAbwEfX3 (privée, à partager depuis le menu Share de la page).

## Organisation

```
echantillon/
  echantillon-fr.jsonl         premier lot, articles FR les plus lus d'octobre 2026, à annoter
scripts/
  preparer_dumps.py            classe les articles par lectures à partir des dumps
  tirer_echantillon.py         tire les articles les plus lus pour l'échantillon annoté
docs/
  differe.md                   travaux différés, à ne pas oublier
  wikimaster/analyse.md        analyse de WikiMasters, le jeu existant le plus proche
  wikipedia/donnees.md         ce que Wikipédia et Wikidata mettent à disposition, mesuré sur de vrais articles
  wikipedia/api.md             comment récupérer ces données : API Action, REST, Wikidata, SPARQL, pageviews, dumps
  gameplay/
    carte/
      type.md                  types de cartes
      budget.md                budget : source, bonus de rareté, dépense
      cout.md                  coût
      rarete.md                rareté
      stats.md                 budget de stats, attaque et défense
      famille.md               familles, utilisées pour les synergies
      illustration.md          image de la carte
      face.md                  ce qui est sur la carte, et la vue détaillée
    synergie/
      index.md                 ce qu'est une synergie, questions générales
      liens.md                 les articles se citent entre eux
      relations.md             relations typées de Wikidata
      epoques.md               dates de vie et d'événements
      categories.md            catégories Wikipédia
    duel.md                    règles d'une partie : deck, tour, combat, victoire
    collection.md              cartes disponibles et boosters
    mecanique/
      index.md                 catalogue fermé des mécaniques : format, construction, noms
      creature.md              mécaniques réservées aux Créatures : mots-clés de combat, stats
      transversal.md           mécaniques ouvertes à tous les types : moments, dégâts, pioche, électricité...
    electricite.md             ressource du jeu
  produit/
    plateforme.md              site web, ordinateur et téléphone
  generation/
    pipeline.md                partage entre code et petit modèle d'assignation
    echantillon.md             articles annotés à la main pour comparer les moteurs d'assignation
    article/
      selection.md             quels articles deviennent des cartes
  ecartees/                    idées écartées, rangées comme le reste de docs/
    gameplay/
      carte/budget.md
      carte/cout.md
      carte/face.md
      carte/famille.md
      carte/illustration.md
      carte/rarete.md
      carte/stats.md
      carte/type.md
      electricite.md
      mecanique/index.md
      synergie/index.md
      synergie/liens.md
      collection.md
      duel.md
      tendance.md
    generation/
      pipeline.md
      article/selection.md
    produit/
      plateforme.md
```
