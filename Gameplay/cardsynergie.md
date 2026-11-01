# Synergies entre cartes

Proposition de départ, à discuter avec Dani. WikiMasters n'a aucune synergie, c'est la partie où on peut le plus se démarquer.

## Familles (couleurs)

Chaque article appartient à plusieurs portails (17 pour la Tour Eiffel : Paris, Architecture et urbanisme, Records, Tourisme, Histoire...). On regroupe les portails en 5 ou 6 familles qui jouent le rôle des couleurs de Magic. Première idée de découpage :

- Histoire et politique
- Sciences et techniques
- Arts et culture
- Géographie et lieux
- Nature et vivant
- Sport et loisirs

Une carte prend une ou deux familles selon ses portails les plus représentés. La Tour Eiffel serait Arts et culture + Géographie. Ça donne naturellement des cartes multicolores, et des effets tribaux ("vos cartes Histoire gagnent +1 en attaque").

Travail à faire : lister les portails de la Wikipédia française et les ranger dans les familles. C'est un mapping manuel à faire une fois.

## Types de cartes

Wikidata dit ce qu'est l'article (`P31`). Ça colle bien aux types de Magic :

| Nature Wikidata | Type de carte | Exemple |
|---|---|---|
| être humain, animal, espèce | Créature | Napoléon Ier, Musaraigne sombre |
| lieu, ville, bâtiment (avec coordonnées GPS) | Terrain, produit le mana de sa famille | Tour Eiffel, District de Koraput |
| bataille, événement, catastrophe | Éphémère ou rituel | Bataille d'Austerlitz |
| œuvre, invention, objet | Artefact | un film, une machine |
| mouvement, idéologie, courant artistique | Enchantement | Romantisme |

Les lieux comme terrains me plaisent beaucoup : un deck Paris joue des terrains parisiens, et on ne sort pas les terrains d'un chapeau.

## Liens entre articles

Le graphe des liens est la donnée la plus originale. Règle possible : une carte reçoit un bonus si un autre article qu'elle cite est sur le champ de bataille.

Problème mesuré : Napoléon a plus de 500 liens sortants et plus de 500 pages qui pointent vers lui. Avec tous les liens, les grosses cartes seraient liées à tout. Pistes pour filtrer :

- ne garder que les liens du résumé introductif (quelques dizaines au maximum, et ce sont les plus importants)
- ne compter un lien que s'il est réciproque (A cite B et B cite A)
- plafonner à N liens par carte

Le lien réciproque pourrait déclencher un effet plus fort, genre "Alliance".

## Relations Wikidata

Plus propres que les liens bruts, parce que typées :

- `P26` conjoint, `P40` enfant, `P22` / `P25` parents : synergie "Famille" (Napoléon + Joséphine de Beauharnais)
- `P1344` a participé à : une créature qui a participé à une bataille la renforce quand on la lance
- `P737` influencé par, `P1066` élève de : "Maître et élève", l'un donne un bonus à l'autre
- `P19` lieu de naissance : une créature est plus forte si son lieu de naissance est un de vos terrains

## Époques

Les dates de naissance et de mort (`P569`, `P570`), ou les dates d'événement, permettent des effets d'époque : "vos créatures du XIXe siècle", ou "Contemporains" quand deux créatures ont vécu en même temps. Ça marche aussi pour les rituels : une bataille ne peut cibler que des créatures vivantes à sa date.

## Catégories

Les catégories visibles sont très fines ("Empereur des Français", "Artilleur", "Décès en mai 1821"). Trop nombreuses pour des mécaniques générales, mais utiles pour des capacités ponctuelles ou des sets thématiques.

## Questions ouvertes

- Familles par portails, ou par types Wikidata ?
- Les synergies se calculent automatiquement pour toutes les cartes, ou on rédige des capacités à la main pour une sélection (comme un set Magic) ? Le calcul automatique donne des dizaines de milliers de cartes jouables. La rédaction manuelle donne des cartes plus intéressantes mais beaucoup moins nombreuses.
- Combien de synergies par carte avant que ce soit illisible ?
