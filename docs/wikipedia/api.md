# API et dumps

Comment récupérer les données décrites dans `wikipedia/donnees.md`. Tous les appels ci-dessous ont été testés le 1er novembre 2026 sur la Wikipédia française, avec "Tour Eiffel", "Napoléon Ier" et "Bataille d'Austerlitz".

## Règles communes

Toutes les API Wikimedia exigent un User-Agent qui identifie le projet et donne un contact, par exemple `wikidado/0.1 (adresse@exemple.fr)`. Sans User-Agent, on reçoit un 403. Un User-Agent générique comme `python-requests/2.31` est refusé aussi, avec un message qui renvoie vers la politique des robots.

Aucune clé n'est nécessaire pour lire. Il n'y a pas de quota chiffré pour l'API Action en lecture : la consigne est de faire les requêtes une par une, sans parallélisme, et d'ajouter `maxlag=5` pour que le serveur nous demande d'attendre quand la base est chargée (il répond alors une erreur `maxlag` au lieu des données).

Les titres s'écrivent avec des underscores ou des espaces, l'API les normalise et l'indique dans un bloc `normalized`.

## API Action (`https://fr.wikipedia.org/w/api.php`)

C'est l'API la plus complète, et la seule qui traite plusieurs articles par appel. Toujours ajouter `format=json&formatversion=2`, qui donne un JSON plus simple (les pages en liste plutôt qu'en dictionnaire indexé par identifiant).

Un appel `action=query` prend jusqu'à 50 titres séparés par `|` (500 pour un compte bot) et combine plusieurs `prop` à la fois. Exemple qui renvoie taille, identifiant Wikidata et description courte pour trois articles :

```
action=query&titles=Napoléon_Ier|Tour_Eiffel|Bataille_d'Austerlitz
  &prop=info|pageprops|description&ppprop=wikibase_item
```

Les `prop` utiles pour le jeu :

| prop | Ce qu'elle donne | Limite par appel |
|---|---|---|
| `info` | taille du wikitexte, dernière révision, `langlinkscount` avec `inprop` | |
| `pageprops` | identifiant Wikidata (`wikibase_item`), présence d'une infobox via les modèles | |
| `description` | description courte, souvent issue de Wikidata | |
| `extracts` | résumé en texte brut (`exintro&explaintext`) | 20 pages, 10 phrases ou 1 200 caractères |
| `pageimages` | image principale | 50 pages |
| `links`, `linkshere` | liens sortants et entrants (`plnamespace=0` pour les articles) | 500 liens |
| `categories` | catégories (`clshow=!hidden` pour les visibles) | 500 |
| `langlinks` | titres dans les autres langues | 500 |
| `pageviews` | lectures par jour | 60 derniers jours |
| `coordinates` | GPS | |
| `cirrusdoc` | document complet de l'index de recherche, voir plus bas | |

Quand une liste dépasse la limite, la réponse contient un bloc `continue` (par exemple `plcontinue` pour les liens) qu'on renvoie tel quel dans l'appel suivant. Les 500 premiers liens de Napoléon Ier tiennent dans un appel, la suite demande une continuation.

`generator=random&grnnamespace=0&grnlimit=N` tire N articles au hasard et applique les `prop` dessus dans le même appel. Pratique pour mesurer des répartitions.

`action=parse&page=Tour_Eiffel&prop=sections|templates` donne la structure de l'article : 76 sections et 253 modèles pour la Tour Eiffel, dont `Modèle:Infobox Monument`. Le nom de l'infobox est un bon indice du type de carte.

### cirrusdoc

`prop=cirrusdoc` renvoie le document que le moteur de recherche indexe pour l'article. Il regroupe en un seul appel des champs qu'il faudrait sinon chercher à plusieurs endroits :

- `incoming_links` : nombre de liens entrants déjà compté (2 152 pour la Tour Eiffel)
- `popularity_score` : part des lectures du wiki, calculée sur les dernières semaines
- `create_timestamp` : date de création de l'article
- `category`, `template`, `outgoing_link`, `heading`, `coordinates`, `wikibase_item`
- `opening_text` et `text` : texte brut, sans wikitexte
- `weighted_tags` : thème et pays prédits par modèle (`articletopic/Geography.Regions.Europe.Western_Europe|766`, `articlecountry/France|1000`), et projets d'évaluation (`pageassessments.project/Patrimoine mondial`)

Les thèmes prédits pourraient servir de premier tri pour les familles (`gameplay/carte/famille.md`).

## API REST

Deux familles d'URL coexistent.

`https://fr.wikipedia.org/api/rest_v1/` est l'ancienne API REST, encore en service. Elle est mise en cache par le CDN (`cache-control: s-maxage=1209600`, réponses servies depuis le cache), donc rapide :

- `page/summary/{titre}` : titre, description, résumé en texte et en HTML, vignette et image originale avec dimensions (2 900 × 5 367 px pour la Tour Eiffel), coordonnées, identifiant Wikidata. C'est l'appel le plus pratique pour afficher une carte.
- `page/media-list/{titre}` : images de l'article (88 pour la Tour Eiffel)
- `feed/featured/{aaaa}/{mm}/{jj}` et `feed/onthisday/events/{mm}/{jj}` : contenu du jour

`https://fr.wikipedia.org/w/rest.php/v1/` est l'API REST de MediaWiki :

- `page/{titre}` : wikitexte complet et licence (159 Ko pour la Tour Eiffel)
- `page/{titre}/bare` : métadonnées sans le contenu
- `page/{titre}/html` : HTML rendu
- `page/{titre}/history/counts/edits` et `/editors` : nombre d'éditions et de contributeurs
- `search/title?q=austerl&limit=3` : autocomplétion de titres, avec description et vignette

La même API existe sous `https://api.wikimedia.org/core/v1/wikipedia/fr/`, où un jeton gratuit donne des quotas plus élevés.

L'API REST ne traite qu'un article par appel. Pour plusieurs milliers d'articles, l'API Action est plus économe.

## Wikidata

`https://www.wikidata.org/w/api.php?action=wbgetentities&ids=Q517|Q243|Q134114&props=labels|descriptions|claims|sitelinks&languages=fr&sitefilter=frwiki` renvoie jusqu'à 50 éléments par appel. Napoléon a 422 propriétés, la Tour Eiffel 180, Austerlitz 52. Les `sitelinks` portent des badges : `Q17437796` signale un article de qualité, `Q17437798` un bon article.

`https://www.wikidata.org/wiki/Special:EntityData/Q517.json` donne l'élément entier (469 Ko pour Napoléon), sans filtrage. À réserver au débogage.

`https://www.wikidata.org/w/rest.php/wikibase/v1/entities/items/Q243/statements?property=P2048` renvoie une seule propriété avec ses qualificatifs. Pour la hauteur de la Tour Eiffel, on obtient plusieurs valeurs datées (la tour a grandi avec les antennes), ce qui oblige à choisir la plus récente ou celle de rang préféré.

### SPARQL

`https://query.wikidata.org/sparql` répond aux requêtes sur tout le graphe. On ajoute `Accept: application/sparql-results+json`. Le délai maximal est de 60 secondes.

Mesures :

- nombre de batailles qui ont un article sur la Wikipédia française : 6 697, en 8 secondes
- nombre d'articles de qualité sur fr via le badge Wikidata : 2 316, en 7 secondes (la catégorie en compte 2 278)
- nombre d'humains qui ont un article sur fr : dépasse le délai, "upstream request timeout" après 65 secondes

Pour les gros comptages, le service QLever (`https://qlever.dev/api/wikidata`) répond à la même syntaxe, à condition de déclarer les préfixes `wd:`, `wdt:` et `schema:`. Il a compté 768 116 humains avec un article sur fr en 6,4 secondes. Il n'est pas géré par Wikimedia et ses données peuvent avoir quelques semaines de retard.

### Ce que Wikidata ne relie pas

Les relations de Wikidata sont plus propres que les liens d'article, mais très incomplètes. Napoléon n'est relié à aucune de ses batailles : sa propriété `P1344` (a participé à) ne contient que "Révolution française", et Austerlitz liste comme participants (`P710`) l'Empire français, la Russie et l'Autriche, sans aucun commandant. Une seule bataille de Wikidata pointe vers Napoléon. Les synergies fondées sur `gameplay/synergie/relations.md` devront compléter avec les liens d'article (`gameplay/synergie/liens.md`).

## Pageviews (`https://wikimedia.org/api/rest_v1/metrics/pageviews/`)

- `per-article/fr.wikipedia/all-access/user/Tour_Eiffel/monthly/20260101/20261031` : lectures par mois (entre 29 744 en août et 50 291 en mai 2026 pour la Tour Eiffel). Granularité `daily` ou `monthly`, historique depuis juillet 2015.
- `top/fr.wikipedia/all-access/2026/10/all-days` : les 1 000 articles les plus lus du mois
- `aggregate/fr.wikipedia/all-access/user/monthly/...` : total du wiki (526 778 192 lectures en octobre 2026)

Le segment `agent` vaut `user`, `automated` ou `spider`. Il faut garder `user` : la Tour Eiffel a 8 331 lectures `automated` en octobre, et le top du mois contient des pages comme `Cookie_(informatique)` en deuxième position (6,1 millions), gonflées par du trafic non humain. Le top devra être filtré avant de servir à quoi que ce soit.

## Lift Wing (`https://api.wikimedia.org/service/lw/inference/v1/models/`)

Modèles de machine learning hébergés par Wikimedia, appelés en POST avec un corps JSON.

- `frwiki-articlequality:predict` avec `{"rev_id": 240706197, "lang": "fr"}` : probabilité de chaque niveau de qualité (e, bd, b, a, ba, adq). La Tour Eiffel sort "adq" à 36 %.
- `outlink-topic-model:predict` avec `{"page_title": "Tour_Eiffel", "lang": "fr"}` : thèmes à partir des liens sortants (`Geography.Regions.Europe.Western_Europe` à 0,74)

Les mêmes prédictions de thème se trouvent déjà dans `cirrusdoc`, sans appel supplémentaire.

## Wikimedia Enterprise

`https://api.enterprise.wikimedia.com/` répond 401 sans compte. L'offre gratuite donne des snapshots mensuels du wiki entier en JSON propre, avec infobox et sections déjà extraites. À regarder si le parsing du wikitexte devient pénible.

## Dumps

Pour générer plusieurs dizaines de milliers de cartes, les dumps évitent des millions d'appels. Tailles au 1er novembre 2026 :

| Fichier | Taille | Contenu |
|---|---|---|
| `frwiki/latest/frwiki-latest-pages-articles-multistream.xml.bz2` | 7,3 Go | wikitexte de tous les articles |
| `frwiki-latest-pagelinks.sql.gz` + `linktarget.sql.gz` | 1,8 Go + 0,35 Go | liens entre pages (la cible passe par la table `linktarget`) |
| `frwiki-latest-categorylinks.sql.gz` | 0,69 Go | catégories |
| `frwiki-latest-langlinks.sql.gz` | 0,39 Go | interwikis |
| `frwiki-latest-page_props.sql.gz` | 0,10 Go | identifiant Wikidata et autres propriétés |
| `other/cirrus_search_index/20261025/index_name=frwiki_content/` | 13,2 Go en plusieurs morceaux | un document `cirrusdoc` par article, en JSON |
| `wikidatawiki/entities/latest-all.json.bz2` | 104 Go | tout Wikidata |
| `wikidatawiki/entities/latest-truthy.nt.bz2` | 44 Go | Wikidata réduit aux valeurs principales, en triplets |
| `other/pageview_complete/monthly/2026/2026-09/pageviews-202609-user.bz2` | 6,3 Go | lectures de tous les wikis pour le mois |

Le dump CirrusSearch est le plus intéressant pour nous. Il est hebdomadaire et contient déjà, article par article, les liens entrants comptés, les catégories, les modèles, le texte brut, l'identifiant Wikidata, les coordonnées et les thèmes prédits. Il ne remplace ni Wikidata pour les relations typées, ni les pageviews pour l'historique de lectures.

Proposition de chaîne de récupération, à confirmer :

1. dump CirrusSearch de frwiki pour la liste des articles et leurs propriétés
2. dump des pageviews pour la popularité sur 12 mois
3. Wikidata filtré sur les seuls éléments qui ont un article fr, à partir du dump truthy ou par `wbgetentities` en lots de 50
4. API Action ou REST seulement pour les mises à jour et pour l'affichage (résumé, image)
