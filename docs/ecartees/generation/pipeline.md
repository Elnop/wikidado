# Idées écartées : génération des cartes

Idées écartées liées à `generation/pipeline.md`.

## Le modèle rédige lui-même le texte des capacités

Écartée le 01/11/2026 : contraire au principe du catalogue fermé de mécaniques.

Un modèle qui rédige librement peut inventer une capacité cassée ou impossible à équilibrer, et le texte de règles devient incohérent d'une carte à l'autre sur des dizaines de milliers de cartes. Le modèle se limite à choisir des mécaniques dans le catalogue, et le texte vient des gabarits.

## Génération une fois par saison seulement

Écartée le 01/11/2026 : génération mixte.

Tout le pool était généré et validé avant la saison, sans génération à la demande.

## Génération à la demande seulement

Écartée le 01/11/2026 : génération mixte.

Une carte était générée la première fois qu'un joueur la tirait, puis gardée. Moins de calcul au départ, mais aucun contrôle global de l'équilibre.

## Pas de trace des versions

Écartée le 01/11/2026 : chaque carte garde la version du catalogue, du modèle et des formules.

On régénérait tout le pool à chaque changement.

## Assignation par une API payante (Jev hébergé, API de LLM)

Écartée le 01/11/2026 : pas de budget, on veut une solution gratuite.

Appeler une API payante (Jev de TypeSafe, ou un LLM hébergé) une fois par article donnerait la meilleure qualité sans infrastructure, mais le coût d'un lot de dizaines de milliers de cartes et la dépendance à un fournisseur ne sont pas acceptables pour l'instant. Le format de questions étant le nôtre, on pourra y revenir sans changer le reste.
