# Idées écartées : sélection des articles

Idées écartées liées à `generation/article/selection.md`.

## Remontée automatique des sous-classes

Écartée le 01/11/2026 : les classes sont choisies à la main.

On prenait toutes les sous-classes de quelques classes racines (lieu géographique, être humain, événement, artefact), avec `P31/P279*`. Plus large, mais avec des intrus.

## Remontée automatique avec liste noire

Écartée le 01/11/2026 : les classes sont choisies à la main.

Remontée automatique, puis une liste de classes à retirer.

## Exclure les personnes vivantes peu connues

Écartée le 01/11/2026 : toutes les personnes vivantes sont gardées.

On gardait les personnalités publiques au-dessus d'un seuil de lectures, et on excluait les personnes vivantes peu connues, pour limiter les problèmes d'image et de droit de la personnalité.

## Exclure toutes les personnes vivantes

Écartée le 01/11/2026 : toutes les personnes vivantes sont gardées.

Seulement des personnes décédées. Évitait les problèmes d'image et de droit de la personnalité, mais retirait les sujets d'actualité.

## Seuil minimal de lectures ou de taille

Écartée le 01/11/2026 : tout article d'une classe retenue devient une carte.

On excluait les articles sous un seuil (nombre de langues, taille, lectures) pour ne garder que ceux qui ont assez de matière pour faire une carte intéressante. Variante : un seuil fixe à 30 lectures par mois, toutes langues confondues.

## Articles sans image libre exclus

Écartée le 01/11/2026 : un article sans image libre reçoit une illustration par défaut.

Un article sans image libre n'était pas une carte. Moins de cartes, mais toutes illustrées. Variante : image obligatoire sauf pour les communes.

## Filtre des articles sensibles

Écartée le 01/11/2026 : les articles sensibles font partie du jeu.

Les articles sur des crimes, des violences sexuelles, des attentats ou des sites pornographiques étaient retirés de la sélection, par catégories Wikipédia et par classes Wikidata.

## Filtre de la fiction

Écartée le 01/11/2026 : la fiction fait partie du jeu.

Les éléments de fiction (armes, lieux, personnages inventés : l'Étoile de la mort) n'étaient pas des cartes. Un filtre transverse retirait tout élément qui descend d'« entité fictionnelle » (`Q14897293`), quelle que soit sa classe : un château fictif est un château, mais n'était pas une carte. Wikidata range aussi sous cette classe les divinités et les personnages mythologiques (divinités grecques, romaines, hindoues), qui étaient donc retirés.

## Racines larges et liste d'exclusions

Écartée le 01/11/2026 : remplacée par une liste blanche de classes fines. Avec des racines larges, tout ce qu'on n'a pas prévu entre dans le jeu, et les exclusions ne voient que les intrus déjà croisés dans l'échantillon, alors que le pool est surtout fait de longue traîne.

Une quarantaine de racines par type, dont des classes larges : occurrence pour Événement, organisation pour Faction, concept pour Savoir, objet artificiel physique pour Objet, position géographique pour Lieu. Chaque article remontait les liens « sous-classe de » jusqu'à 12 sauts, et prenait le type de la racine la plus proche. Douze classes étaient exclues : entité fictionnelle, jeu vidéo, film, série de films, œuvre littéraire, album, single, série télévisée, saison de série télévisée, programme télévisé, page d'homonymie, page de liste.

Erreurs relevées : le Pape classé Objet (titre honorifique, puis distinction), le procès de Nuremberg classé Savoir (concept), Mai 68 classé Faction (mouvement social, puis groupe d'humains), le STEN et Harry Potter classés Savoir (objet mathématique), la Ligue des champions classée Faction (ligue, puis organisation). La racine concept ramenait des séries télévisées, des pages de liste et un mème. Exclure « œuvre créative » aurait retiré la tour Eiffel, Big Ben et la Joconde.

## « Dehors » sans effet sur l'héritage

Écartée le 01/11/2026 : la classe choisie la plus proche gagne, même si elle est marquée dehors.

Dès qu'une classe retenue était atteinte, l'article devenait une carte. Les classes marquées dehors servaient seulement à noter les classes examinées et laissées de côté.

## Remontée courte

Écartée le 02/11/2026 : les racines apprises sont hautes, et leur pureté est vérifiée sur toute la remontée.

Un article n'était retenu que si sa classe était dans la liste ou en descendait par quelques liens « sous-classe de » au plus (piste : 3 sauts), pour moins dépendre du désordre de la hiérarchie de Wikidata.

## Liste blanche remplie classe par classe

Écartée le 02/11/2026 : trop long, la longue traîne compte des milliers de classes. Remplacée par les racines apprises à partir des classes déjà choisies.

On choisissait le type de chaque classe `P31` de l'échantillon une par une (928 classes pour 2 963 articles), en partant des plus fréquentes.
