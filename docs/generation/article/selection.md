# Sélection des articles

Quels articles Wikipédia deviennent des cartes. Le type de carte que donne chaque nature d'article est décrit dans `gameplay/carte/type.md`.

## Reconnaître la nature d'un article

Wikidata donne la nature d'un élément avec la propriété `P31` ("nature de l'élément"). La Tour Eiffel est une tour, Napoléon est un être humain (Q5).

Attention : `P31` pointe vers la classe la plus précise. Une église est `P31` église, et pas `P31` bâtiment. Pour récupérer tous les bâtiments, il faut remonter la hiérarchie des sous-classes (`P31/P279*` en SPARQL). Sinon on rate une grosse partie des articles. Exemples mesurés : seulement 90 articles fr sont directement `P31` maladie, 409 directement `P31` événement, 37 directement `P31` outil et 156 directement `P31` lieu géographique. Ces classes générales sont presque toujours atteintes par sous-classe.

## Liste des classes retenues

Les classes Wikidata qui donnent des cartes sont choisies à la main, avec pour chacune le type de carte qu'elle donne (église, château, musée, tour... pour Terrain). On contrôle ce qui entre dans le jeu, et la liste sert aussi à fixer la famille de chaque classe (voir `gameplay/carte/famille.md`). Il faut la maintenir quand on ajoute des types d'articles.

## Volumes sur la Wikipédia française

Nombre d'articles fr dont l'élément Wikidata a directement cette classe en `P31`. Mesuré le 1er novembre 2026 avec le SPARQL Wikidata.

| Classe | Articles fr |
|---|---|
| taxon (espèces, genres...) | 149 895 |
| album | 29 427 |
| église | 17 339 |
| rivière | 13 685 |
| single | 10 664 |
| montagne | 7 969 |
| bataille | 6 697 |
| ville | 5 945 |
| musée | 4 722 |
| château | 4 660 |
| club de football | 8 405 |
| parti politique | 5 536 |
| université | 2 138 |
| logiciel | 1 293 |
| discipline académique | 1 238 |
| opération militaire | 910 |
| profession | 870 |
| mouvement artistique | 475 |
| aliment | 234 |
| pays | 210 |
| élément chimique | 156 |
| outil | 37 |
| vêtement | 31 |

Les très grosses classes (être humain, film, commune de France, œuvre littéraire) ont dépassé le délai du service de requête. Il faudra les compter à partir du dump Wikidata. Pour les humains, on parle de plusieurs centaines de milliers d'articles.

Il y a largement assez d'articles pour chaque type. Les taxons à eux seuls pèsent 150 000 articles, dont la plupart sont des ébauches sur des insectes ou des araignées.

## Pas de seuil minimal

Tout article d'une classe retenue devient une carte, même sans aucune lecture. Les articles peu lus deviennent des communes (voir `gameplay/carte/rarete.md`). Le pool de communes sera énorme, avec beaucoup d'articles pauvres en données.

Un article sans image libre reste une carte, avec une illustration par défaut (voir `gameplay/carte/illustration.md`).

## Articles à exclure d'office

- listes, homonymies, années ("2008 en archéologie"), saisons sportives
- œuvres (films, albums, livres, singles), voir `gameplay/carte/type.md`
- articles sensibles : crimes, violences sexuelles, attentats. À filtrer par catégories et par classes Wikidata.

Les personnes vivantes sont gardées, sans exclusion spécifique.
