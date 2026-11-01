# Génération des cartes

On définit nous-mêmes un catalogue fermé de mécaniques, puis un petit modèle choisit lesquelles donner à chaque article. Le modèle ne fait que de l'assignation, il n'invente ni règle ni texte de capacité.

## Partage du travail entre code et modèle

Tout ce qui se calcule à partir des données doit être fait par du code, pas par le modèle. C'est reproductible, gratuit, et on peut rééquilibrer en changeant une formule puis en régénérant.

Le code s'occupe de :

- sélectionner les articles (classes Wikidata, exclusions, voir `generation/article/selection.md`)
- fixer le type de carte à partir de la classe Wikidata (voir `gameplay/carte/type.md`)
- calculer la rareté (voir `gameplay/carte/rarete.md`)
- calculer le budget de base, le coût et le budget effectif (voir `gameplay/carte/budget.md` et `gameplay/carte/cout.md`)
- après l'assignation, répartir le reste du budget dans les stats (voir `gameplay/carte/stats.md`)
- calculer les sous-types et les familles à partir de Wikidata (voir `gameplay/carte/type.md` et `gameplay/carte/famille.md`)
- trouver les cibles des synergies : liens réciproques, relations Wikidata, époque, lieu de naissance

Le modèle s'occupe uniquement de ce qui demande de comprendre le sujet :

- choisir des mécaniques dans le catalogue qui collent à l'article, dans la limite du budget effectif (une bataille éclair aura plutôt "Rapidité", un château plutôt "Fortification")
- choisir les paramètres d'une mécanique quand il y en a ("+1 aux créatures Militaires")
- choisir la répartition des stats entre attaque et défense, à partir de la répartition par défaut du code (voir `gameplay/carte/stats.md`)
- éventuellement, choisir la phrase du résumé à afficher comme texte d'ambiance

## Pipeline

1. Extraction : depuis les dumps, on construit une fiche par article retenu (titre, résumé, classe Wikidata, propriétés utiles, lectures, taille, contributeurs, liens du résumé).
2. Calcul : le code ajoute le type, les sous-types, les familles, la rareté, le budget de base, le coût, le budget effectif et la liste des synergies possibles.
3. Assignation : le modèle reçoit la fiche, le budget effectif et le catalogue des mécaniques autorisées pour ce type. Il répond en JSON contraint, avec uniquement des identifiants du catalogue.
4. Validation : le code vérifie que les mécaniques existent, que les paramètres sont valides et que la somme des `cout_budget` ne dépasse pas le budget effectif. Une carte qui ne passe pas est régénérée.
5. Stats : le code met le reste du budget effectif dans les stats, avec la répartition choisie par le modèle.
6. Rendu : le texte de la carte est produit à partir des gabarits du catalogue, jamais par le modèle.

Exemple de sortie attendue du modèle :

```json
{
  "article": "Q517",
  "mecaniques": [
    { "id": "inspiration", "params": { "cible": "militaires" } },
    { "id": "participant", "params": { "evenement": "Q134114" } }
  ]
}
```

## Traçabilité

Chaque carte garde la version du catalogue de mécaniques, du modèle et des formules (budget, coût, rareté) qui l'ont produite. Quand on change l'un des trois, on ne régénère que les cartes concernées.

## Moment de la génération

Génération mixte. Un pool de base est généré et validé avant chaque saison, ce qui permet de vérifier l'équilibre avant de publier. Les articles hors de ce pool sont générés à la demande, la première fois qu'un joueur tire la carte, puis gardés.

## Pourquoi un catalogue fermé

Avec un catalogue fermé, le modèle ne peut pas inventer une capacité cassée. Il peut seulement mal choisir, et une mauvaise assignation se repère et se corrige. Le texte de règles reste homogène sur des dizaines de milliers de cartes, et chaque mécanique a un coût en budget défini une fois pour toutes. Un petit modèle suffit aussi, parce que choisir dans une liste est beaucoup plus simple que rédiger.

## Choix du modèle

Contrainte : pas de budget, tout doit tourner gratuitement et sur CPU (pas de GPU). Le modèle est donc local, petit, et appelé en lot.

L'assignation se pose comme des questions typées sur la fiche de l'article, dans le style des modèles de décision (Jev, OpenJev) :

- choix unique : une mécanique parmi celles autorisées pour le type de carte (le catalogue est découpé pour rester sous une cinquantaine d'options par question, si besoin en chaînant plusieurs questions)
- oui/non : une mécanique précise convient-elle à l'article ?
- score : intensité d'une dimension, sur des niveaux décrits par des situations

Chaque réponse garde sa probabilité. Une réponse peu confiante part en relecture humaine au lieu d'être acceptée. Le format des questions et des réponses est le nôtre (JSON), indépendant du modèle derrière, pour pouvoir changer de moteur sans toucher au catalogue.

Moteurs possibles, à comparer sur un échantillon de 200 à 300 articles qu'on annote nous-mêmes (taux d'accord avec nos choix) :

- embeddings sur CPU : similarité entre la fiche et la description de chaque mécanique, plus kNN sur des cartes annotées
- petit LLM quantifié sur CPU (llama.cpp) avec sortie JSON contrainte, en lot
- modèle de décision ouvert type OpenJev, trop lourd pour du CPU seul (27 milliards de paramètres, licence non commerciale)
