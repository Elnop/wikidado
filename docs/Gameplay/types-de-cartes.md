# Types de cartes

On ne garde que certaines natures d'articles, et chaque nature retenue donne un type de carte. Les noms des types ne sont pas encore choisis, ceux ci-dessous sont des exemples.

| Type (provisoire) | Ce que ça couvre | Rôle en jeu (à définir) |
|---|---|---|
| Terrain | lieux avec coordonnées : villes, montagnes, rivières, bâtiments | produit des ressources |
| Créature | personnes, animaux | se bat sur le terrain |
| Événement | batailles, opérations militaires, catastrophes | effet ponctuel, comme un éphémère ou un rituel |
| Technique | inventions, outils, logiciels, disciplines | effet permanent, comme un artefact ou un enchantement |

## Comment reconnaître la nature d'un article

Wikidata donne la nature d'un élément avec la propriété `P31` ("nature de l'élément"). La Tour Eiffel est une tour, Napoléon est un être humain (Q5).

Attention : `P31` pointe vers la classe la plus précise. Une église est `P31` église, et pas `P31` bâtiment. Pour récupérer tous les bâtiments, il faut remonter la hiérarchie des sous-classes (`P31/P279*` en SPARQL). Sinon on rate une grosse partie des articles. Exemples mesurés : seulement 90 articles fr sont directement `P31` maladie, 409 directement `P31` événement, 37 directement `P31` outil et 156 directement `P31` lieu géographique. Ces classes générales sont presque toujours atteintes par sous-classe.

On a deux façons de faire :

- une liste de classes Wikidata choisies à la main par type de carte (église, château, musée, tour... pour Terrain). On contrôle bien ce qui entre, mais il faut maintenir la liste.
- une remontée automatique vers quelques classes racines (lieu géographique, être humain, événement, artefact). C'est plus large, mais il y aura des intrus.

Je partirais sur la liste à la main : c'est plus facile à équilibrer et on sait ce qu'on met dans le jeu.

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

Ce qui en ressort : il y a largement assez d'articles pour chaque type. Le problème sera de réduire. Les taxons à eux seuls pèsent 150 000 articles, dont la plupart sont des ébauches sur des insectes ou des araignées. On peut fixer un seuil (nombre de langues, taille, lectures) pour ne garder que les articles qui ont assez de matière pour faire une carte intéressante.

## Articles à exclure d'office

- listes, homonymies, années ("2008 en archéologie"), saisons sportives
- articles sensibles : crimes, violences sexuelles, attentats, personnes vivantes peu connues. À filtrer par catégories et par classes Wikidata.
- articles sans image libre, si on décide que chaque carte doit avoir une illustration

## Questions ouvertes

- Combien de types au total ? Quatre comme Magic (sans compter les planeswalkers), ou plus ?
- Les œuvres (films, albums, livres) entrent-elles dans un type, ou on les laisse de côté au début ?
- Les espèces sont-elles des Créatures, comme les humains, ou un type à part ?
- Les personnes vivantes posent un problème d'image et de droit de la personnalité. On les garde ?
