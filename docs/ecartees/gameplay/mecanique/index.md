# Idées écartées : mécaniques

Idées écartées liées à `gameplay/mecanique/index.md`.

## Mécanique qui ajoute du mana (cout_mana)

Écartée le 01/11/2026 : une mécanique consomme seulement du budget (cout_budget).

Chaque mécanique avait un cout_mana ajouté directement au coût de la carte, et le budget de stats se calculait sur le coût total sans rien retirer.

## Mécanique qui ajoute du mana et consomme du budget

Écartée le 01/11/2026 : une mécanique consomme seulement du budget.

Une mécanique avait à la fois un cout_mana et un cout_budget. Plus fin, mais deux chiffres à régler et un risque de double comptage : la capacité faisait monter le coût, donc le budget, puis en reprenait une partie.

## Coût fixe quels que soient les paramètres

Écartée le 01/11/2026 : le cout_budget dépend de la valeur des paramètres.

Une mécanique avait un seul cout_budget. Plus simple, mais "+1 aux créatures Histoire" coûtait autant que "+1 à toutes vos créatures".

## Une mécanique par variante de paramètre

Écartée le 01/11/2026 : le cout_budget dépend de la valeur des paramètres, dans une seule mécanique.

Chaque version devenait une mécanique à part dans le catalogue (inspiration-famille, inspiration-globale), chacune avec son coût.

## Nombre maximum de mécaniques selon la rareté

Écartée le 01/11/2026 : pas de maximum, seul le budget limite.

Par exemple commune 2, peu commune 3, rare 4, mythique 5.

## Nombre maximum de mécaniques fixe

Écartée le 01/11/2026 : pas de maximum, seul le budget limite.

Même limite pour toutes les cartes, par exemple 3.

## Retirer les mécaniques de stats

Écartée le 01/11/2026 : elles restent, pour orienter une carte vers l'attaque ou la défense.

Elles ne servaient qu'à permettre les grosses cartes sans capacité, ce que le budget fait maintenant tout seul.

## Production d'électricité réservée aux Lieux

Écartée le 01/11/2026 : tous les types peuvent produire de l'électricité.

La mécanique centrale ne pouvait être donnée qu'à un Lieu (centrale, barrage, mine).

## Production d'électricité pour les Lieux et les Techniques

Écartée le 01/11/2026 : tous les types peuvent produire de l'électricité.

Une centrale (Lieu) ou une machine (Technique) pouvait produire, mais pas une Créature ni un Événement.

## Catalogue construit seulement à partir des articles

Écartée le 01/11/2026 : on part des actions de base du jeu, puis on teste sur les articles de l'échantillon.

On prenait chaque article de l'échantillon, on imaginait ses mécaniques, puis on regroupait le tout en catalogue. Risque : des mécaniques taillées pour les articles les plus lus, qui couvrent mal le reste du pool.

## Catalogue construit seulement à partir des règles

Écartée le 01/11/2026 : on part des actions de base du jeu, puis on teste sur les articles de l'échantillon.

On listait les actions possibles par type de carte sans regarder les articles. Risque : un Magic générique, sans lien avec Wikipédia.

## Catalogue de 20 ou 40 mécaniques en première version

Écartée le 01/11/2026 : la première version vise environ 80 mécaniques.

20 mécaniques suffisaient pour lancer l'annotation et un prototype. 40 donnaient six à huit mécaniques par type, plus faciles à équilibrer et à choisir pour un petit modèle.

## Noms de mots-clés repris de Magic et Hearthstone

Écartée le 01/11/2026 : les mots-clés ont des noms propres au jeu.

Célérité, Piétinement, Provocation... Les joueurs de Magic comprenaient tout de suite.

## Catalogue dans un seul fichier

Écartée le 01/11/2026 : un dossier `gameplay/mecanique/`, avec un fichier par type de carte.

On gardait `gameplay/mecanique.md` avec une section par type.
