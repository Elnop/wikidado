# Mots-clés

Capacités de combat à prix fixe. La plupart sont réservées aux Créatures, Bouc émissaire va aussi aux Lieux. Les autres types peuvent donner ces mots-clés avec l'effet continu `mot-cle-donne` (voir `gameplay/mecanique/effet.md`).

La liste des mots-clés, avec leur texte, les types qui peuvent les recevoir, leur prix, leur indice et leur statut (retenu ou proposé), est dans `config/mecanique/mot-cle.json`. Mots-clés actuels : Préparé, Débordement, Initiative, Imblocable, Pillage, Sentinelle, Toxique, Bouc émissaire.

## Bouc émissaire

Une Créature Bouc émissaire peut être visée par une attaque, comme un Lieu (voir `gameplay/duel.md`). Tant qu'un joueur contrôle une carte Bouc émissaire, les attaquants adverses doivent viser une de ses cartes Bouc émissaire plutôt que lui ou ses autres Lieux. S'il en a plusieurs, l'attaquant choisit laquelle. Le défenseur peut toujours bloquer normalement.
