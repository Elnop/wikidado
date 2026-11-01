# Synergies entre cartes

WikiMasters n'a aucune synergie, c'est la partie où on peut le plus se démarquer.

Une synergie est un effet qui se déclenche selon les autres cartes en jeu. Les synergies sont calculées automatiquement pour toutes les cartes : le code trouve les cibles possibles (liens, relations Wikidata, époques), puis le modèle assigne les mécaniques correspondantes (voir `generation/pipeline.md`). Les sources de synergie sont décrites chacune dans leur fichier :

- `gameplay/synergie/liens.md` : les articles se citent entre eux
- `gameplay/synergie/relations.md` : relations typées de Wikidata (famille, maître et élève, participation, lieu de naissance)
- `gameplay/synergie/epoques.md` : dates de vie et d'événements
- `gameplay/synergie/categories.md` : catégories Wikipédia
- `gameplay/carte/famille.md` : effets tribaux par famille

## Questions ouvertes

- Combien de synergies par carte avant que ce soit illisible ?
