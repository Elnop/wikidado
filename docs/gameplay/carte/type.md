# Types de cartes

On ne garde que certaines natures d'articles, et chaque nature retenue donne un type de carte. Il y a 4 types. Leurs noms ne sont pas encore choisis, ceux ci-dessous sont des exemples.

Le découpage en 4 est à vérifier sur ce que Wikipédia et Wikidata proposent : chaque type doit couvrir assez d'articles intéressants (voir les volumes dans `generation/article/selection.md`). Le choix des articles est décrit dans `generation/article/selection.md`.

Les œuvres (films, albums, livres) ne sont pas des cartes pour la première version. On reverra la question une fois les 4 types vérifiés.

| Type (provisoire) | Ce que ça couvre | Rôle en jeu (à définir) |
|---|---|---|
| Terrain | lieux avec coordonnées : villes, montagnes, rivières, bâtiments | produit des ressources |
| Créature | personnes, espèces animales et végétales | se bat sur le terrain |
| Événement | batailles, opérations militaires, catastrophes | effet ponctuel, comme un éphémère ou un rituel |
| Technique | inventions, outils, logiciels, disciplines | effet permanent, comme un artefact ou un enchantement |

## Sous-types

Comme dans Magic, chaque carte a un type (un des 4) et des sous-types, en nombre illimité. Les sous-types sont calculés par le code à partir de Wikidata :

- la nature de l'élément (`P31`) : Église, Château, Bataille, Cheval
- pour les personnes, les occupations (`P106`) : Militaire, Homme politique, Peintre

Napoléon serait une Créature avec les sous-types Humain, Homme politique, Militaire, Monarque. Il y a autant de sous-types possibles que de classes et d'occupations dans Wikidata.

Les familles sont des groupes de sous-types (voir `gameplay/carte/famille.md`).

## Correspondance avec Magic

Wikidata dit ce qu'est l'article (`P31`). Ça colle bien aux types de Magic :

| Nature Wikidata | Type Magic | Exemple |
|---|---|---|
| être humain, animal, espèce | Créature | Napoléon Ier, Musaraigne sombre |
| lieu, ville, bâtiment (avec coordonnées GPS) | Terrain, produit du mana | Tour Eiffel, District de Koraput |
| bataille, événement, catastrophe | Éphémère ou rituel | Bataille d'Austerlitz |
| invention, objet | Artefact | une machine |
| mouvement, idéologie, courant artistique | Enchantement | Romantisme |

Les lieux comme terrains me plaisent beaucoup : un deck Paris joue des terrains parisiens, et on ne sort pas les terrains d'un chapeau.
