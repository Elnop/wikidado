# Catalogue des mécaniques

Liste fermée des mécaniques que le modèle peut assigner aux cartes (voir `generation/pipeline.md`). Aucune mécanique n'est validée pour l'instant.

La première version vise environ 80 mécaniques. La plupart sont ouvertes à tous les types de carte. Quelques-unes sont réservées à certains types à cause de leur nature : une mécanique qui modifie les stats de la carte ne va qu'aux types qui ont des stats, un équipement ne va qu'aux Objets.

- `gameplay/mecanique/transversal.md` : mécaniques ouvertes à tous les types
- `gameplay/mecanique/creature.md` : mécaniques réservées aux Créatures, dont les mots-clés de combat

D'autres fichiers par type (`lieu.md`, `objet.md`, `faction.md`...) seront ajoutés dans le même dossier si des mécaniques leur sont réservées.

## Moments

Une mécanique peut agir à trois moments : quand la carte est jouée (À la une), quand elle est détruite (Postérité), ou en continu tant qu'elle est en jeu. Un Événement n'a que le premier. Le détail est dans `gameplay/mecanique/transversal.md`.

## Application selon le type

Une mécanique ouverte à tous les types garde le même texte partout. Les règles du type s'appliquent par-dessus : sur une Faction, un effet qui touche vos Créatures ne touche que les Créatures affectées à cette Faction (voir `gameplay/duel.md`).

## Construction du catalogue

On commence par les mécaniques ouvertes à tous les types, puis les mécaniques réservées. On part des actions de base du jeu (dégâts, pioche, bonus de stats, destruction, protection, électricité, défausse, affectation aux Factions) pour poser un squelette. On le teste ensuite sur les articles de l'échantillon (voir `generation/echantillon.md`) : pour chaque article, on cherche les mécaniques qu'on lui donnerait. Un article qui ne trouve rien de juste montre un trou dans le catalogue, une mécanique que personne ne prend est à revoir.

## Noms

Les mots-clés ont des noms propres au jeu, avec une saveur Wikipédia ou électrique, même quand l'effet existe déjà dans Magic ou Hearthstone (vol, piétinement, provocation). Le texte complet de l'effet est toujours affiché dans la vue détaillée (voir `gameplay/carte/face.md`).

## Format d'une mécanique

Chaque mécanique doit préciser :

- `id` : identifiant stable, utilisé dans le JSON du modèle
- `texte` : gabarit du texte affiché sur la carte, avec ses paramètres entre accolades
- `types` : types de cartes qui peuvent la recevoir
- `cout_budget` : points de budget qu'elle consomme dans le budget effectif de la carte (voir `gameplay/carte/budget.md`). Quand la mécanique a des paramètres, le coût est donné pour chaque valeur : "+1 aux créatures Histoire" coûte moins que "+1 à toutes vos créatures".
- `params` : paramètres possibles et leurs valeurs autorisées
- `condition` : données nécessaires dans la fiche de l'article (par exemple, la mécanique n'est proposée que si l'article a un lieu de naissance)
- `indice` : une phrase pour aider le modèle à choisir (à quel genre d'article elle va bien)

Les mécaniques dont les paramètres viennent des données (terre-natale, participant) peuvent se passer du modèle. Le modèle sert surtout pour les mécaniques "de saveur" comme inspiration, où il faut comprendre le sujet.

## Pistes

- Étalon de prix : 1 point de budget vaut 1 point de stat. robuste suit déjà cette règle (2 points pour +2 en défense). Le prix d'une mécanique se fixerait en la comparant aux stats que la carte aurait reçues à la place.
- Ajouter au format un champ qui dit si la mécanique est assignée par le code ou par le modèle.
- Chaque mécanique assignée par le modèle doit pouvoir se décider à partir de la fiche (résumé, classes, propriétés Wikidata).

## Données exploitables pour des capacités

- label "Article de qualité" ou "Bon article" : mot-clé de rareté ou capacité bonus (6 600 articles sur fr, assez rare pour être spécial)
- âge de l'article (création en 2003 pour Napoléon) : mot-clé "Ancien" ?
- coordonnées GPS : l'article est un lieu, voir `gameplay/carte/type.md` pour les Lieux
- importance "maximum" dans un projet : carte iconique de sa famille

## À faire

- lister les mécaniques par type de carte
- fixer le coût en budget de chacune après des parties de test
