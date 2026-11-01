# Types de cartes

On ne garde que certaines natures d'articles, et chaque nature retenue donne un type de carte. Il y a 6 types : Lieu, Créature, Événement, Objet, Savoir et Faction.

Le découpage en 6 est à vérifier sur ce que Wikipédia et Wikidata proposent : chaque type doit couvrir assez d'articles intéressants (voir les volumes dans `generation/article/selection.md`). Le choix des articles est décrit dans `generation/article/selection.md`.

Les œuvres (films, albums, livres, jeux vidéo) ne sont pas des cartes.

Les règles de la partie sont dans `gameplay/duel.md`.

| Type | Ce que ça couvre | Rôle en jeu |
|---|---|---|
| Lieu | lieux avec coordonnées : villes, montagnes, rivières, bâtiments. Aussi les lieux virtuels : sites web, plateformes en ligne, réseaux sociaux | a une défense et peut être attaqué à la place du joueur, ne bloque pas |
| Créature | personnes, espèces animales et végétales | se bat, a une attaque et une défense |
| Événement | batailles, opérations militaires, catastrophes | effet ponctuel joué à son tour, comme un rituel |
| Objet | outils, armes, véhicules, machines, instruments, vêtements | reste en jeu avec ses propres mécaniques, peut s'attacher à une Créature, comme un artefact |
| Savoir | disciplines, sciences, théories, technologies, logiciels, langages, idéologies, mouvements artistiques | reste en jeu sans capacité propre, agit sur les autres cartes et sur les règles, comme un enchantement |
| Faction | organisations : partis politiques, entreprises, clubs de sport, groupes de musique, groupes d'humains | reste en jeu sans capacité propre, ses effets ne touchent que les Créatures qu'on lui affecte |

## Sous-types

Comme dans Magic, chaque carte a un type (un des 6) et des sous-types, en nombre illimité. Les sous-types sont calculés par le code à partir de Wikidata :

- la nature de l'élément (`P31`) : Église, Château, Bataille, Cheval
- pour les personnes, les occupations (`P106`) : Militaire, Homme politique, Peintre
- pour les espèces, la classification : on remonte les taxons parents (`P171`) jusqu'à quelques rangs choisis, comme la classe et l'ordre. La Musaraigne sombre, que `P31` décrit seulement comme Taxon, devient aussi Mammifère et Eulipotyphle

Napoléon serait une Créature avec les sous-types Humain, Homme politique, Militaire, Monarque. Il y a autant de sous-types possibles que de classes et d'occupations dans Wikidata.

Les familles sont des groupes de sous-types (voir `gameplay/carte/famille.md`).

## Correspondance avec Magic

Wikidata dit ce qu'est l'article (`P31`). Ça colle bien aux types de Magic :

| Nature Wikidata | Type Magic | Exemple |
|---|---|---|
| être humain, animal, espèce | Créature | Napoléon Ier, Musaraigne sombre |
| lieu, ville, bâtiment (avec coordonnées GPS), site web, réseau social | proche d'un Terrain, mais ne sert pas de ressource de base | Tour Eiffel, District de Koraput, Wikipédia |
| bataille, événement, catastrophe | Éphémère ou rituel | Bataille d'Austerlitz |
| outil, arme, véhicule, machine, objet fabriqué | Artefact (type Objet) | une machine |
| discipline, théorie, technologie, idéologie, courant artistique | Enchantement (type Savoir) | Romantisme |
| parti, entreprise, club, groupe de musique | proche d'un enchantement, limité à ses membres (type Faction) | Parti socialiste, FC Barcelone |

Un deck Paris joue des Lieux parisiens.

## Choix du type d'un article

Un article a plusieurs classes Wikidata (`P31`). Son type est celui de la classe racine la plus proche d'une de ses classes, en comptant les liens « sous-classe de » (`P279`). À distance égale, l'ordre Créature, Lieu, Événement, Objet, Savoir, Faction départage. Les éléments de fiction (armes, lieux, personnages inventés) ne sont pas des cartes.
