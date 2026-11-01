# Conditions

La condition dit ce qu'il faut pour que la capacité marche : une carte en jeu, ou un état de la partie. Elle est facultative, et sert surtout aux synergies (voir `gameplay/synergie/index.md`). Une condition remplie par le code ne demande rien au modèle.

La liste des conditions est dans `config/mecanique/condition.json`, avec leur texte, leur facteur, ce qui les remplit (le modèle ou le code), les données Wikidata utilisées et leur statut. Les conditions remplies par le code viennent des relations de l'article : lieu de naissance (`P19`), famille (`P26`, `P40`, `P22`, `P25`), maître (`P1066`, `P737`), liens entre articles, liens réciproques (alliance, la capacité va aussi à l'autre carte), dates (contemporain).

Exemple, Napoléon Ier né à Ajaccio : "Tant que vous contrôlez Ajaccio, cette Créature gagne +2 en attaque." Effet bonus-attaque 2, cible cette-carte, condition terre-natale : 2 × 1 × 0,5 = 1.
