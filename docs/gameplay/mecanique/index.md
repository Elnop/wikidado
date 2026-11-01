# Catalogue des mécaniques

Liste fermée de ce que le modèle peut assigner aux cartes (voir `generation/pipeline.md`). Les briques et leurs prix sont retenus pour la première version. Tout ce qui est dans la config est retenu : une brique pas encore tranchée reste dans la doc comme piste, et n'entre dans la config qu'une fois validée. Tous les prix restent à régler en partie de test.

Une mécanique est soit un mot-clé, soit une capacité composée de briques. Le catalogue fermé est celui des briques : le modèle ne peut assembler que des briques qui existent, et le code calcule le prix et le texte de l'assemblage.

- `gameplay/mecanique/mot-cle.md` : mots-clés de combat (Préparé, Imblocable, Bouc émissaire...)
- `gameplay/mecanique/declencheur.md` : quand une capacité déclenchée agit
- `gameplay/mecanique/effet.md` : ce que fait la capacité, effets ponctuels et effets continus
- `gameplay/mecanique/cible.md` : sur qui l'effet porte, et les filtres qui restreignent la cible
- `gameplay/mecanique/condition.md` : ce qu'il faut avoir en jeu pour que la capacité marche, dont les synergies tirées des données

## Config

La liste des briques, leurs textes, leurs prix et leurs facteurs sont dans `config/mechanics/`, en JSON. C'est la config qui fait foi : la doc explique les règles, la config donne les valeurs. Le pipeline de génération et le jeu lisent les mêmes fichiers.

- un fichier par brique : `keyword.json`, `trigger.json`, `effect.json`, `duration.json`, `target.json`, `filter.json`, `condition.json`
- `cost.json` : arrondi et minimum du prix d'une capacité

La liste des types de cartes est dans `config/card/type.json`. Son schéma définit l'énumération des types, que tous les autres schémas réutilisent.
- `schema/` : un JSON Schema par fichier, plus `card-mechanics.schema.json` pour les mécaniques assignées à une carte (sortie du modèle, annotations de l'échantillon)

Les textes sont rangés par langue (`"text": { "fr": "..." }`). Tout ce qui est propre au code (noms de fichiers, clés, identifiants des briques) est en anglais ; les textes affichés au joueur et les indices pour le modèle sont en français.

`generation/check_mechanics.py` (`uv run check_mechanics.py` depuis `generation/`) valide la config contre les schémas, vérifie les renvois entre fichiers et recalcule les exemples de prix de cette doc. Avec des fichiers JSON Lines en argument, il vérifie aussi les mécaniques de chaque carte : briques connues, cibles et valeurs autorisées, type de carte compatible.

## Deux sortes de capacités

Une capacité déclenchée agit une fois, à un moment précis :

```
déclencheur : effet ponctuel + cible (+ filtre) (+ condition)
À la une : infligez 3 dégâts à une Créature Militaire adverse.
Quand elle attaque : piochez 1 carte.
```

Une capacité passive agit en continu, tant que la carte est en jeu. Elle n'a pas de déclencheur :

```
effet continu + cible (+ filtre) (+ condition)
Vos Créatures Sport gagnent +1 en attaque.
Tant que vous contrôlez Ajaccio, cette Créature gagne +1 en attaque.
```

Un Événement ne reste pas en jeu : il n'a que des capacités déclenchées, avec le déclencheur À la une.

## Prix d'une capacité

Chaque brique a un prix ou un facteur. Le prix d'une capacité est le produit :

```
cout_budget = arrondi_superieur(cout_effet × facteur_duree × facteur_cible × facteur_filtre × facteur_declencheur × facteur_condition) + ajout_declencheur
```

Le résultat vaut au moins 1. Les capacités passives n'ont pas de facteur de déclencheur. Postérité fait exception à la multiplication : elle retire 1 au prix, c'est son `ajout` (voir `gameplay/mecanique/declencheur.md`).

Étalon : 1 point de budget vaut 1 point de stat. Le prix d'un effet se fixe en le comparant aux stats que la carte aurait reçues à la place.

Un mot-clé a un prix fixe, donné dans `config/mechanics/keyword.json`.

## Application selon le type

La plupart des briques vont à tous les types de carte. Quelques-unes sont réservées à cause de leur nature, et chaque fichier le précise : un bonus de stats sur la carte elle-même ne va qu'aux Créatures et aux Lieux, le déclencheur "quand elle attaque" ne va qu'aux Créatures.

Un Lieu reçoit toujours au moins une capacité (voir `gameplay/carte/budget.md`).

Une capacité garde le même texte quel que soit le type. Les règles du type s'appliquent par-dessus : sur une Faction, un effet qui touche vos Créatures ne touche que les Créatures affectées à cette Faction (voir `gameplay/duel.md`).

## Assignation par le modèle

Le modèle répond par une suite de questions enchaînées (voir `generation/pipeline.md`) : quel effet convient à l'article, puis sur quelle cible, puis avec quel déclencheur. Chaque brique a un indice (`hint`) qui l'aide à choisir. Les briques remplies par le code (cartes liées, époques) n'ont pas besoin du modèle.

Exemple de sortie pour Napoléon Ier :

```json
{
  "article": "Q517",
  "mechanics": [
    { "trigger": "on-play", "effect": "damage", "n": 2, "target": "all-opponents", "filter": { "type": "creature" } },
    { "effect": "attack-bonus", "n": 1, "target": "your-others", "filter": { "family": "militaire" } },
    { "keyword": "first-strike" }
  ]
}
```

## Construction du catalogue

On commence par les briques ouvertes à tous les types, puis les briques réservées. On part des actions de base du jeu (dégâts, pioche, bonus de stats, destruction, protection, électricité, défausse, affectation aux Factions). On teste ensuite sur les articles de l'échantillon (voir `generation/echantillon.md`) : pour chaque article, on cherche les capacités qu'on lui donnerait. Un article qui ne trouve rien de juste montre un trou dans le catalogue, une brique que personne ne prend est à revoir.

Le nombre de briques n'est pas un objectif : on en ajoute quand le test sur l'échantillon montre un trou.

## Noms

Les mots-clés ont des noms propres au jeu, avec une saveur Wikipédia ou électrique, même quand l'effet existe déjà dans Magic ou Hearthstone (vol, piétinement, provocation). Le texte complet de chaque capacité est affiché dans la vue détaillée (voir `gameplay/carte/face.md`).

## Données exploitables pour des capacités

- label "Article de qualité" ou "Bon article" : mot-clé de rareté ou capacité bonus (6 600 articles sur fr, assez rare pour être spécial)
- âge de l'article (création en 2003 pour Napoléon) : mot-clé "Ancien" ?
- coordonnées GPS : l'article est un lieu, voir `gameplay/carte/type.md` pour les Lieux
- importance "maximum" dans un projet : carte iconique de sa famille

## À faire

- tester le catalogue sur les articles de l'échantillon
- fixer les prix et les facteurs après des parties de test
