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

## Catalogue réparti surtout par type

Écartée le 01/11/2026 : la plupart des mécaniques sont ouvertes à tous les types, seules quelques-unes sont réservées à cause de leur nature.

Les 80 mécaniques étaient réparties par type : Créature environ 22, Événement 14, Savoir 12, Lieu 10, Objet 10, Faction 8, et 6 transversales. Deux variantes : environ 12 par type, ou une vingtaine de synergies transversales au détriment des types.

## Commencer le catalogue par les Créatures ou par les Événements

Écartée le 01/11/2026 : on commence par les mécaniques ouvertes à tous les types.

Les Créatures étaient le type le plus courant, et leurs mots-clés auraient servi de base aux autres. Les Événements avaient des effets simples à chiffrer. Autre option : un premier jet grossier de tous les types en même temps.

## Effets à l'arrivée seulement, ou aucun déclencheur

Écartée le 01/11/2026 : il y a des effets à l'arrivée en jeu (À la une) et à la destruction (Postérité).

Seulement l'arrivée, plus simple à lire et à calculer pour l'IA. Ou aucun déclencheur, uniquement des effets permanents et des mots-clés.

## Dépêche, nom du mot-clé qui permet d'attaquer tout de suite

Écartée le 01/11/2026 : le mot-clé s'appelle Préparé.

"Dépêche : peut attaquer le tour où elle est jouée", par référence aux dépêches de presse.

## Autres prix des moments

Écartées le 01/11/2026 : Postérité coûte 1 de moins qu'À la une, Chaque tour coûte 3 fois plus.

Chaque tour à 2 fois le prix, pour voir plus souvent des effets récurrents. Postérité au même prix qu'À la une, sans réduction pour l'effet à la destruction.

## Catalogue en liste de mécaniques fixes

Écartée le 01/11/2026 : les capacités se composent de briques (déclencheur, effet, cible, filtre, condition), seuls les mots-clés restent une liste fixe.

Chaque mécanique était une entrée complète du catalogue, avec son texte, ses paramètres et son prix. Le premier jet de cette liste est gardé dans `ecartees/gameplay/mecanique/transversal.md` et `ecartees/gameplay/mecanique/creature.md`. Une variante gardait les briques pour les capacités déclenchées seulement, et une liste fixe pour les passives.

## Prix d'une capacité par additions ou par table

Écartée le 01/11/2026 : le prix est le produit des facteurs des briques.

Par additions : coût de l'effet + supplément de cible + supplément de déclencheur, plus simple à lire mais moins juste pour les gros effets. Par table : prix fixé à la main pour chaque combinaison autorisée, le plus précis mais avec beaucoup de chiffres.

## Imblocable bloquée par les autres Imblocables

Écartée le 01/11/2026 : une carte Imblocable ne peut pas être bloquée du tout.

Comme le Vol de Magic, deux cartes Imblocables pouvaient se bloquer entre elles, pour un prix de 2.

## Autres noms pour le mot-clé Imblocable

Écartée le 01/11/2026 : le mot-clé s'appelle Imblocable.

Insaisissable, Viral (saveur internet), Aérien (le plus proche du Vol), Clandestin (espions, fugitifs), Hors d'atteinte.

## Autres prix pour les mots-clés

Écartées le 01/11/2026 : Préparé 1, Débordement 1, Initiative 2, Imblocable 3, Pillage 2, Sentinelle 1, Toxique 2.

Préparé à 2, parce qu'attaquer tout de suite surprend l'adversaire. Initiative à 1, parce que sans dégâts persistants entre les tours l'effet compte surtout en défense. Imblocable à 4, ou réservé aux Créatures qui ont 3 ou moins en attaque. Pillage à 1, parce que les points de vie pèsent peu avec 30 au départ. Toxique à 1 ou 3.

## Prestige, et autres noms pour Pillage

Écartée le 01/11/2026 : le mot-clé qui rend des points de vie s'appelle Pillage.

Prestige, Ferveur, Rayonnement, Ovation, Charisme.

## Autres noms pour Bouc émissaire

Écartée le 01/11/2026 : le mot-clé s'appelle Bouc émissaire.

Paratonnerre (thème électrique), Point de mire, Provocation (le nom de Hearthstone).

## Bouc émissaire limité au blocage ou aux mécaniques

Écartée le 01/11/2026 : une Créature Bouc émissaire est à la fois une cible d'attaque prioritaire et la cible obligée des mécaniques adverses à cible unique.

Bloque en premier : tant qu'elle peut bloquer, le défenseur doit l'assigner à un attaquant avant tout autre bloqueur. Attire les mécaniques : seules les mécaniques adverses à cible unique doivent la cibler.

## Sentinelle remplacée par la Provocation

Écartée le 01/11/2026 : Sentinelle reste, et Bouc émissaire s'ajoute à côté.

## Vigilance et Résistant

Écartés le 01/11/2026 : pas retenus pour la première version.

Vigilance ("peut attaquer puis bloquer au tour adverse") est déjà vrai pour toutes les Créatures dans les règles du duel. Résistant : la première fois qu'elle devrait être détruite, elle survit avec 1 en défense (survivants, phénix, institutions qui renaissent).

## Autres facteurs pour les déclencheurs

Écartées le 01/11/2026 : Quand elle attaque × 2, Quand elle bloque × 1,5, Quand elle subit des dégâts × 1,5, Quand une carte arrive en jeu ou est détruite × 2.

Quand elle attaque à × 2,5, parce qu'elle attaque presque à chaque tour. Quand elle bloque à × 1, ou retiré comme trop rare. Quand elle subit des dégâts à × 1, ou retiré. Pour les déclencheurs sur les autres cartes : filtre obligatoire, ou × 3 quand il n'y a pas de filtre.
