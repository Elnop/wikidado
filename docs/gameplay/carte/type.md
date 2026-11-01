# Types de cartes

On ne garde que certaines natures d'articles, et chaque nature retenue donne un type de carte. Il y a 4 types. Leurs noms ne sont pas encore choisis, ceux ci-dessous sont des exemples.

Le découpage en 4 est à vérifier sur ce que Wikipédia et Wikidata proposent : chaque type doit couvrir assez d'articles intéressants (voir les volumes dans `generation/article/selection.md`). Le choix des articles est décrit dans `generation/article/selection.md`.

| Type (provisoire) | Ce que ça couvre | Rôle en jeu (à définir) |
|---|---|---|
| Terrain | lieux avec coordonnées : villes, montagnes, rivières, bâtiments | produit des ressources |
| Créature | personnes, animaux | se bat sur le terrain |
| Événement | batailles, opérations militaires, catastrophes | effet ponctuel, comme un éphémère ou un rituel |
| Technique | inventions, outils, logiciels, disciplines | effet permanent, comme un artefact ou un enchantement |

## Correspondance avec Magic

Wikidata dit ce qu'est l'article (`P31`). Ça colle bien aux types de Magic :

| Nature Wikidata | Type Magic | Exemple |
|---|---|---|
| être humain, animal, espèce | Créature | Napoléon Ier, Musaraigne sombre |
| lieu, ville, bâtiment (avec coordonnées GPS) | Terrain, produit du mana | Tour Eiffel, District de Koraput |
| bataille, événement, catastrophe | Éphémère ou rituel | Bataille d'Austerlitz |
| œuvre, invention, objet | Artefact | un film, une machine |
| mouvement, idéologie, courant artistique | Enchantement | Romantisme |

Les lieux comme terrains me plaisent beaucoup : un deck Paris joue des terrains parisiens, et on ne sort pas les terrains d'un chapeau.

## Questions ouvertes

- Les œuvres (films, albums, livres) entrent-elles dans un type, ou on les laisse de côté au début ?
- Les espèces sont-elles des Créatures, comme les humains, ou un type à part ?
