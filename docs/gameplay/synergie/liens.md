# Synergie par liens entre articles

Le graphe des liens est la donnée la plus originale. Règle possible : une carte reçoit un bonus si un autre article qu'elle cite est sur le champ de bataille.

Problème mesuré : Napoléon a plus de 500 liens sortants et plus de 500 pages qui pointent vers lui. Avec tous les liens, les grosses cartes seraient liées à tout. Pistes pour filtrer :

- ne garder que les liens du résumé introductif (quelques dizaines au maximum, et ce sont les plus importants)
- ne compter un lien que s'il est réciproque (A cite B et B cite A)
- plafonner à N liens par carte

Le lien réciproque pourrait déclencher un effet plus fort, genre "Alliance".
