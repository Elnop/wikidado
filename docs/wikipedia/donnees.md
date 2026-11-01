# Données disponibles

Tout a été testé le 1er novembre 2026 sur la Wikipédia française, principalement avec "Napoléon Ier" et "Tour Eiffel".

## Par article

| Donnée | Exemple | Où la récupérer |
|---|---|---|
| Titre, description courte, résumé, image principale | "militaire, homme d'État et monarque français", portrait par David | REST `/api/rest_v1/page/summary/{titre}` |
| Lectures par jour | Napoléon : environ 2 500 par jour, environ 76 000 sur octobre 2026 | `prop=pageviews` (60 derniers jours), API Pageviews pour l'historique |
| Taille du wikitexte | Napoléon : 260 796 octets | `prop=info` |
| Nombre de langues | Napoléon : 221 interwikis, 288 sitelinks Wikidata | `prop=langlinks`, ou `langlinkscount` dans `prop=info` |
| Liens sortants vers d'autres articles | Napoléon : plus de 500 | `prop=links&plnamespace=0` |
| Articles qui pointent vers celui-ci | Napoléon : plus de 500 | `prop=linkshere` |
| Nombre d'éditions et de contributeurs | Napoléon : 5 599 éditions, 1 944 contributeurs | REST `/w/rest.php/v1/page/{titre}/history/counts/edits` et `/editors` |
| Date de création | Napoléon : 17 janvier 2003 | `prop=revisions&rvdir=newer&rvlimit=1` |
| Catégories visibles | "Empereur des Français", "Artilleur", "Décès en mai 1821" | `prop=categories&clshow=!hidden` |
| Portails | Tour Eiffel : 17 portails (Paris, Architecture et urbanisme, Records, Tourisme...) | catégories cachées `Catégorie:Portail:X/Articles liés` |
| Avancement et importance par projet | Tour Eiffel : avancement A, importance maximum pour Architecture, Culture, France | catégories de la page `Discussion:{titre}` |
| Label qualité | 2 278 "Article de qualité" et 4 329 "Bon article" sur fr | `Catégorie:Article de qualité`, `Catégorie:Bon article` |
| Qualité prédite par modèle | Napoléon : "adq" avec 29 % de probabilité | Lift Wing, modèle `frwiki-articlequality` |
| Coordonnées GPS | Tour Eiffel : 48.858, 2.294 | `prop=coordinates` |
| Nombre d'images | Tour Eiffel : 120 | `prop=images` |
| Identifiant Wikidata | Napoléon : Q517 | `pageprops.wikibase_item` |

## Wikidata

Napoléon a 422 propriétés. Celles qui servent probablement le plus :

- `P31` nature de l'élément (Q5 = être humain, et pour les autres : bâtiment, bataille, ville, espèce, film...)
- `P569` / `P570` dates de naissance et de mort
- `P19` / `P20` lieux de naissance et de mort
- `P106` occupation (Napoléon : homme politique, militaire, monarque)
- `P27` nationalité
- `P18` image
- `P2048` taille (Napoléon : 168 cm)
- `P26` conjoint, `P40` enfant, `P22` / `P25` parents
- `P1344` a participé à, `P737` influencé par, `P1066` élève de

Les relations entre éléments sont typées, ce qui les rend plus propres que les liens bruts de l'article.

## Données globales

- 2 787 648 articles sur la Wikipédia française (`meta=siteinfo`)
- Flux quotidien : articles les plus lus, image du jour, actualités, éphéméride (52 événements pour un 1er novembre) via `/api/rest_v1/feed/featured/{aaaa}/{mm}/{jj}` et `/feed/onthisday/events/{mm}/{jj}`
- Top des articles les plus lus par mois via l'API Pageviews. En octobre 2026, on y trouve beaucoup de personnalités de la présidentielle 2027 (David Lisnard, Raphaël Glucksmann, Sarah Knafo).

## Répartition sur un échantillon aléatoire

Sur 50 articles tirés au hasard : taille médiane 5,4 Ko, 6 à 7 langues en médiane, et une dizaine d'articles qui n'existent qu'en français.

Lectures sur octobre 2026 pour quelques-uns :

| Article | Lectures | Langues |
|---|---|---|
| Linothele molleturo (araignée) | 0 | 0 |
| District de Koraput | 3 | 33 |
| NGC 4266 | 7 | 24 |
| Musaraigne sombre | 13 | 27 |
| William Empson | 63 | 17 |
| Caribou (musicien) | 180 | 13 |
| Nabih Berri | 678 | 21 |
| Marcel Ophuls | 897 | 26 |
| Irène Jacob | 18 353 | 37 |
| Michèle Laroque | 31 205 | 24 |
| Napoléon Ier | environ 76 000 | 221 |

La grande majorité des articles a très peu de lecteurs. Toute formule devra passer par un logarithme.

## Contraintes

Licence : le texte est sous CC BY-SA 4.0 (attribution obligatoire, partage à l'identique pour le texte repris). Les images de Commons ont chacune leur licence, à vérifier fichier par fichier.

API : mettre un User-Agent identifiable avec un contact, et rester raisonnable sur le débit. Sur les appels en rafale, l'API Pageviews renvoie parfois une erreur au lieu du JSON. Le paramètre `prop=pageviews` en mode batch ne renvoie les vues que pour une partie des pages.

Pour construire une base de plusieurs dizaines de milliers de cartes, il vaut mieux partir des dumps (https://dumps.wikimedia.org/ : wikitexte, liens, catégories, Wikidata en JSON, pageviews) que d'appeler l'API article par article.

Contenu sensible : certains articles portent sur des crimes, de la violence ou de la sexualité. Ils sont gardés dans le jeu (voir `generation/article/selection.md`).
