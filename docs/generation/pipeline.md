# Génération des cartes

On définit nous-mêmes un catalogue fermé de mécaniques, puis un petit modèle choisit lesquelles donner à chaque article. Le modèle ne fait que de l'assignation, il n'invente ni règle ni texte de capacité.

## Partage du travail entre code et modèle

Tout ce qui se calcule à partir des données doit être fait par du code, pas par le modèle. C'est reproductible, gratuit, et on peut rééquilibrer en changeant une formule puis en régénérant.

Le code s'occupe de :

- sélectionner les articles (classes Wikidata, seuils, exclusions, voir `generation/article/selection.md`)
- fixer le type de carte à partir de la classe Wikidata (voir `gameplay/carte/type.md`)
- calculer la rareté (voir `gameplay/carte/rarete.md`)
- après l'assignation, calculer le coût à partir des mécaniques choisies (voir `gameplay/carte/cout.md`), puis le budget et les stats (voir `gameplay/carte/stats.md`)
- calculer la famille à partir des classes Wikidata (voir `gameplay/carte/famille.md`)
- trouver les cibles des synergies : liens réciproques, relations Wikidata, époque, lieu de naissance

Le modèle s'occupe uniquement de ce qui demande de comprendre le sujet :

- choisir 0 à N mécaniques dans le catalogue qui collent à l'article (une bataille éclair aura plutôt "Rapidité", un château plutôt "Fortification")
- choisir les paramètres d'une mécanique quand il y en a ("+1 aux créatures de famille X")
- éventuellement, choisir la phrase du résumé à afficher comme texte d'ambiance

## Pipeline

1. Extraction : depuis les dumps, on construit une fiche par article retenu (titre, résumé, classe Wikidata, propriétés utiles, lectures, taille, contributeurs, liens du résumé).
2. Calcul : le code ajoute le type, la rareté, la famille et la liste des synergies possibles.
3. Assignation : le modèle reçoit la fiche et le catalogue des mécaniques autorisées pour ce type. Il répond en JSON contraint, avec uniquement des identifiants du catalogue.
4. Validation : le code vérifie que les mécaniques existent, que les paramètres sont valides et que le coût obtenu reste dans la plage autorisée. Une carte qui ne passe pas est régénérée ou reçoit une mécanique par défaut.
5. Coût et stats : le code calcule le coût à partir des mécaniques, puis le budget et les stats à partir du coût et de la rareté.
6. Rendu : le texte de la carte est produit à partir des gabarits du catalogue, jamais par le modèle.

Exemple de sortie attendue du modèle :

```json
{
  "article": "Q517",
  "mecaniques": [
    { "id": "inspiration", "params": { "famille": "histoire" } },
    { "id": "maitre-de-guerre" }
  ]
}
```

## Moment de la génération

Génération mixte. Un pool de base est généré et validé avant chaque saison, ce qui permet de vérifier l'équilibre avant de publier. Les articles hors de ce pool sont générés à la demande, la première fois qu'un joueur tire la carte, puis gardés.

## Pourquoi un catalogue fermé

Avec un catalogue fermé, le modèle ne peut pas inventer une capacité cassée. Il peut seulement mal choisir, et une mauvaise assignation se repère et se corrige. Le texte de règles reste homogène sur des dizaines de milliers de cartes, et chaque mécanique a un coût en mana et en budget défini une fois pour toutes. Un petit modèle suffit aussi, parce que choisir dans une liste est beaucoup plus simple que rédiger.

## Choix du modèle

À tester sur un échantillon de 200 à 300 articles qu'on annote nous-mêmes. On compare plusieurs modèles sur le taux d'accord avec nos choix et le coût par carte. Pour 50 000 cartes, même un modèle léger appelé une fois par carte reste peu cher. On pourra aussi regrouper plusieurs fiches par appel.

## Questions ouvertes

- Nombre maximum de mécaniques par carte selon le coût ?
- On garde une trace de quelle version du catalogue et du modèle a produit chaque carte, pour pouvoir régénérer proprement ?
