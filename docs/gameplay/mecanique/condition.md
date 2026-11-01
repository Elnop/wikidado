# Conditions

La condition dit ce qu'il faut avoir en jeu pour que la capacité marche. Elle est facultative, et sert surtout aux synergies (voir `gameplay/synergie/index.md`). Une condition remplie par le code ne demande rien au modèle.

| id | texte | facteur | rempli par | données |
|---|---|---|---|---|
| controle-type | "tant que vous contrôlez un {type ou famille}" | × 0,75 | le modèle | aucune |
| terre-natale | "tant que vous contrôlez {lieu}" | × 0,5 | le code | `P19` (lieu de naissance) qui existe comme carte Lieu |
| lignee | "tant que vous contrôlez {proche}" | × 0,5 | le code | `P26` (conjoint), `P40` (enfant), `P22` / `P25` (parents) vers une carte Créature |
| maitre | "tant que vous contrôlez {maître}" | × 0,5 | le code | `P1066` (élève de) ou `P737` (influencé par) vers une carte Créature |
| reference | "tant que vous contrôlez {carte}" | × 0,5 | le code | un article cité par l'article (voir `gameplay/synergie/liens.md`) |
| alliance | "tant que vous contrôlez {carte}", et la même capacité est donnée à l'autre carte | × 0,75 | le code | les deux articles se citent l'un l'autre |
| contemporain | "tant que vous contrôlez une carte de la même époque" | × 0,5 | le code | l'article a des dates (voir `gameplay/synergie/epoques.md`) |

Exemple, Napoléon Ier né à Ajaccio : "Tant que vous contrôlez Ajaccio, cette Créature gagne +2 en attaque." Effet bonus-attaque 2, cible cette-carte, condition terre-natale : 2 × 1 × 0,5 = 1.
