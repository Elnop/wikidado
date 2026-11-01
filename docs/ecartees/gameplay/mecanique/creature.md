# Mécaniques des Créatures

Écartée le 01/11/2026 : les capacités se composent de briques (déclencheur, effet, cible, filtre, condition) au lieu d'une liste de mécaniques fixes. Voir `gameplay/mecanique/index.md`. Les effets, les noms et les indices ci-dessous ont été repris dans les briques.

Format et règles communes dans `gameplay/mecanique/index.md`. Ces mécaniques ne vont qu'aux Créatures, parce qu'elles touchent au combat ou aux stats de la carte, ou parce que leurs données n'existent que pour des personnes. Premier jet : les noms, les textes et les coûts sont des propositions.

Les autres types peuvent donner ces mots-clés à des Créatures avec la mécanique transmission (voir `gameplay/mecanique/transversal.md`).

## Mots-clés de combat

| id | texte | cout_budget | indice |
|---|---|---|---|
| prepare | "Préparé : peut attaquer le tour où elle est jouée." | 1 | personnes rapides, réactives, sportifs, reporters, cavalerie |
| debordement | "Débordement : quand elle est bloquée, les dégâts en trop atteignent sa cible." | 1 | personnes ou animaux massifs, irrésistibles, chefs de guerre offensifs |
| initiative | "Initiative : inflige ses dégâts de combat avant les autres Créatures." | 2 | duellistes, tireurs, stratèges, prédateurs |
| insaisissable | "Insaisissable : ne peut être bloquée que par des Créatures insaisissables." | 2 | oiseaux, aviateurs, espions, fugitifs, personnes difficiles à saisir |
| prestige | "Prestige : quand elle inflige des dégâts, vous gagnez autant de points de vie." | 2 | personnes très admirées, champions, idoles |
| sentinelle | "Sentinelle : peut bloquer deux attaquants." | 1 | gardiens, défenseurs, policiers, gardiens de but |

## Mécaniques de stats

Le reste du budget va déjà aux stats (voir `gameplay/carte/stats.md`), donc ces mécaniques ne sont pas nécessaires pour faire une grosse carte sans capacité : elles servent au modèle à orienter une carte vers l'attaque ou la défense.

| id | texte | cout_budget | effet | indice |
|---|---|---|---|---|
| robuste | aucun, la mécanique s'affiche seulement dans les stats de la carte | 2 | +2 en défense | sujets solides, durables, difficiles à abattre |
| offensif | aucun, la mécanique s'affiche seulement dans les stats de la carte | 2 | +2 en attaque | sujets agressifs, conquérants, prédateurs |

## Synergies tirées des données

Remplies par le code à partir de Wikidata (voir `gameplay/synergie/relations.md`). Le modèle n'a pas à juger.

| id | texte | params | cout_budget | condition |
|---|---|---|---|---|
| terre-natale | "Tant que vous contrôlez {lieu}, cette Créature gagne +1/+1." | lieu, rempli avec `P19` (lieu de naissance) | 1 | l'article a un `P19` qui existe comme carte Lieu |
| participant | "Quand vous jouez {evenement}, piochez une carte." | événement, rempli avec `P1344` (a participé à) | 1 | l'article a un `P1344` qui existe comme carte Événement |
| lignee | "Tant que vous contrôlez {proche}, cette Créature gagne +1/+1." | proche, rempli avec `P26` (conjoint), `P40` (enfant), `P22` / `P25` (parents) | 1 | l'article a un de ces liens vers une carte Créature |
| maitre-eleve | "Tant que vous contrôlez {maitre}, cette Créature gagne +1 en attaque et vous piochez une carte quand elle arrive en jeu." | maître, rempli avec `P1066` (élève de) ou `P737` (influencé par) | 2 | l'article a un de ces liens vers une carte Créature |
