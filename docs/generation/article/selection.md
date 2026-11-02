# Sélection des articles

Quels articles Wikipédia deviennent des cartes. Le type de carte que donne chaque nature d'article est décrit dans `gameplay/carte/type.md`.

## Reconnaître la nature d'un article

Wikidata donne la nature d'un élément avec la propriété `P31` ("nature de l'élément"). La Tour Eiffel est une tour, Napoléon est un être humain (Q5).

Attention : `P31` pointe vers la classe la plus précise. Une église est `P31` église, et pas `P31` bâtiment. Exemples mesurés : seulement 90 articles fr sont directement `P31` maladie, 409 directement `P31` événement, 37 directement `P31` outil et 156 directement `P31` lieu géographique. Les classes générales sont presque toujours atteintes par sous-classe (`P279`), mais la hiérarchie de Wikidata est trop emmêlée pour s'y fier sur une longue distance : la tour Eiffel descend d'« œuvre créative », le pistolet-mitrailleur STEN d'« objet mathématique ».

## Liste blanche des classes retenues

La liste dit quelles classes Wikidata donnent des cartes, avec pour chacune un type de carte ou « dehors ». Elle contient deux sortes d'entrées :

- des classes choisies à la main : église, château pour Lieu ; parti politique, club de football pour Faction ; discipline, idéologie pour Savoir ;
- des racines apprises : les classes les plus hautes sous lesquelles toutes les classes déjà choisies ont le même type (voir plus bas). Elles classent d'un coup les classes qu'on n'a pas encore vues.

Une classe large n'entre dans la liste que si elle est pure sur l'échantillon et validée à la main. Entité cartographiable donne Lieu sans exception notable ; organisation et concept mélangent les types et restent dehors.

Une classe n'entre dans la liste que si elle est reliée à « entité » (`Q35120`), la classe la plus haute de Wikidata, par une chaîne complète de liens « sous-classe de » (`P279`). Certaines classes n'ont aucun « sous-classe de » et restent isolées (Web 2.0, orbite de la Lune, régime monarchique) : elles ne sont pas retenues.

- Un article est retenu si une de ses classes `P31` est dans la liste, ou en descend par les liens « sous-classe de » (`P279`), sans limite de sauts.
- Tout ce que la liste n'atteint pas reste dehors. Une classe oubliée coûte quelques cartes, un intrus ne passe pas.
- Le type de l'article vient de la classe retenue la plus proche (voir `gameplay/carte/type.md`). Une classe choisie à la main est plus proche que la racine au-dessus d'elle, donc elle gagne.
- Une classe peut aussi être marquée « dehors ». Elle sert d'exception sous une classe retenue : la classe choisie la plus proche gagne, même si c'est « dehors », et l'article n'est alors pas une carte. Saison sportive est dehors alors que compétition sportive, plus haut, donne Événement. Question ouverte : que faire quand une classe dehors et une classe retenue sont à la même distance ?
- La liste sert aussi à fixer la famille de chaque classe (voir `gameplay/carte/famille.md`).
- Les classes choisies sont exportées dans `scripts/liste-blanche.json`, avec pour chaque classe son type ou « dehors », qui l'a choisie et quand.

### Racines apprises

On ne choisit pas toutes les classes une par une : la longue traîne en compte des milliers. On procède en trois temps.

1. On choisit à la main les classes les plus fréquentes de l'échantillon, sur une page partagée (https://claude.ai/artifact/QMRMjTfwfJW4nZ9LTfqTMH).
2. Un script remonte la hiérarchie de toutes ces classes et cherche les ancêtres les plus hauts qui sont purs : au moins 2 classes choisies sous eux, et au moins 90 % d'entre elles du même type. Il les prend dans l'ordre où ils expliquent le plus de choix encore non expliqués.
3. Chaque racine candidate est validée ou rejetée à la main, sur une page qui montre les classes choisies qu'elle explique, ses exceptions (classes choisies d'un autre type sous elle, qui restent dans la liste et gagnent), et les classes pas encore vues qu'elle classerait.

Mesuré le 2 novembre 2026 sur l'échantillon de 2 963 articles, avec 342 classes choisies : 30 racines typent 74 % des articles, et 98 % des articles déjà choisis qu'elles atteignent reçoivent le bon type. Au-delà, chaque racine de plus ne gagne que quelques articles.

Certaines racines pures ont un nom sans rapport avec le jeu (« physical property value » pour des Créatures) : la pureté est mesurée, mais la validation à la main reste nécessaire.

### Filtres transverses

Deux filtres coupent à travers tous les types et s'appliquent quelle que soit la classe retenue, avec une remontée complète :

- les pages de liste (`Q13406463`) ;
- les pages d'homonymie (`Q4167410`).

La fiction n'est pas filtrée. Les éléments de fiction (personnages, lieux, armes inventés, et les divinités, que Wikidata range sous « entité fictionnelle ») deviennent des cartes quand leur classe est dans la liste blanche, avec le type de cette classe.

### Rapport de couverture

Un outil liste les classes `P31` des articles non retenus, triées par nombre d'articles, sur un échantillon qui mélange les plus lus et un tirage au hasard dans la longue traîne. On choisit les plus fréquentes, puis on recalcule les racines apprises et on relance pour voir la couverture monter.

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

## Articles qui ne sont pas des cartes

Retirés par les filtres transverses :

- listes et homonymies

Absents de la liste blanche, donc jamais retenus :

- années ("2008 en archéologie") et saisons sportives

Les personnes vivantes sont gardées, sans exclusion spécifique.

Les articles sensibles (crimes, meurtriers, attentats, violences, sexualité, sites pornographiques) sont gardés comme les autres.
