# Registre des idées

Toutes les idées du projet, y compris celles qu'on a écartées. On ne supprime jamais une idée : quand on l'abandonne, on passe son statut à "écartée" et on note pourquoi et quand. Comme ça on sait ce qui a déjà été envisagé, et on peut ressortir une idée si le contexte change.

Statuts :

- à discuter : proposée, pas encore tranchée
- retenue : décidée par Leon et Dani
- écartée : abandonnée, avec la raison

Quand une idée est détaillée dans un autre document, la colonne "Détail" pointe vers lui. Les chemins partent de `docs/`.

## Génération des cartes

| Idée | Statut | Détail | Notes |
|---|---|---|---|
| Définir un catalogue fermé de mécaniques, puis un petit modèle qui ne fait que les assigner aux articles | retenue (1/11/2026) | `Generation/pipeline.md`, `Gameplay/mecaniques.md` | |
| Le code calcule tout ce qui se déduit des données (type, coût, stats, famille, cibles de synergie), le modèle ne fait que le choix des mécaniques | à discuter | `Generation/pipeline.md` | |
| Le modèle rédige lui-même le texte des capacités | écartée (1/11/2026) | | Contraire au principe du catalogue fermé : risque de capacités cassées et de texte de règles incohérent |
| Construire la base à partir des dumps plutôt que de l'API | à discuter | `Wikipedia/donnees-disponibles.md` | |

## Types de cartes

| Idée | Statut | Détail | Notes |
|---|---|---|---|
| Ne garder que certaines natures d'articles, chacune donne un type de carte | retenue (1/11/2026) | `Gameplay/types-de-cartes.md` | Noms des types pas encore choisis |
| Types Terrain / Créature / Événement / Technique | à discuter | `Gameplay/types-de-cartes.md` | Noms donnés comme exemples |
| Sélection par liste de classes Wikidata choisies à la main | à discuter | `Gameplay/types-de-cartes.md` | Recommandée face à la remontée automatique |
| Sélection par remontée automatique vers quelques classes racines | à discuter | `Gameplay/types-de-cartes.md` | Plus large, mais avec des intrus |
| Les lieux avec coordonnées GPS sont des terrains qui produisent le mana de leur famille | à discuter | `Gameplay/cardsynergie.md` | |
| Seuil minimal (langues, taille, lectures) pour qu'un article devienne une carte | à discuter | `Gameplay/types-de-cartes.md` | |

## Coût et stats

| Idée | Statut | Détail | Notes |
|---|---|---|---|
| Stats qui montent avec la notoriété, comme WikiMasters | écartée (1/11/2026) | `Wikimaster/analyse.md` | La carte la plus célèbre gagne toujours, aucun intérêt tactique |
| Coût fixé par la notoriété (lectures + langues), stats réparties dans un budget lié au coût | à discuter | `Gameplay/cardcost.md` | |
| Attaque selon la taille, défense selon le nombre de contributeurs, en relatif à coût égal | à discuter | `Gameplay/cardcost.md` | |
| Coûts figés pour une saison | à discuter | `Gameplay/cardcost.md` | |
| Bonus "Tendance" quand l'article est dans les plus lus de la semaine | à discuter | `Gameplay/cardcost.md` | |
| Rareté séparée du coût, basée sur les lectures | à discuter | `Gameplay/cardcost.md` | |
| Label "Article de qualité" / "Bon article" comme mot-clé ou capacité | à discuter | `Gameplay/cardcost.md` | |

## Synergies

| Idée | Statut | Détail | Notes |
|---|---|---|---|
| Familles (couleurs) à partir des portails | à discuter | `Gameplay/cardsynergie.md` | |
| Synergie quand deux articles se citent, limitée aux liens du résumé ou aux liens réciproques | à discuter | `Gameplay/cardsynergie.md` | |
| Synergies par relations Wikidata (famille, maître et élève, participation, lieu de naissance) | à discuter | `Gameplay/cardsynergie.md` | |
| Effets d'époque à partir des dates | à discuter | `Gameplay/cardsynergie.md` | |

## Duel

| Idée | Statut | Détail | Notes |
|---|---|---|---|
| Duel sous forme de quiz, comme WikiMasters | écartée (1/11/2026) | `Wikimaster/analyse.md` | Le projet veut un vrai gameplay de cartes à la Magic |
