#!/usr/bin/env python3
import argparse
import json
import math
import os
import sys

RACINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "config", "mecanique")
FICHIERS = {
    "mot-cle": "mots_cles",
    "declencheur": "declencheurs",
    "effet": "effets",
    "duree": "durees",
    "cible": "cibles",
    "filtre": "filtres",
    "condition": "conditions",
}


def charger_json(chemin):
    with open(chemin, encoding="utf-8") as f:
        return json.load(f)


def valider_schemas(erreurs):
    try:
        import jsonschema
        from referencing import Registry, Resource
    except ImportError:
        print("jsonschema absent : validation des schémas sautée (pip install jsonschema)")
        return
    dossier = os.path.join(RACINE, "schema")
    ressources = []
    for nom in os.listdir(dossier):
        ressources.append((nom, Resource.from_contents(charger_json(os.path.join(dossier, nom)))))
    registre = Registry().with_resources(ressources)
    for nom in list(FICHIERS) + ["prix"]:
        schema = charger_json(os.path.join(dossier, f"{nom}.schema.json"))
        validateur = jsonschema.Draft202012Validator(schema, registry=registre)
        for e in validateur.iter_errors(charger_json(os.path.join(RACINE, f"{nom}.json"))):
            erreurs.append(f"{nom}.json : {e.message}")


def charger_catalogue():
    catalogue = {nom: {e["id"]: e for e in charger_json(os.path.join(RACINE, f"{nom}.json"))[cle]} for nom, cle in FICHIERS.items()}
    catalogue["prix"] = charger_json(os.path.join(RACINE, "prix.json"))
    return catalogue


def verifier_references(cat, erreurs):
    for e in cat["effet"].values():
        for c in e["cibles"]:
            if c not in cat["cible"]:
                erreurs.append(f"effet {e['id']} : cible inconnue {c}")
        if e["sorte"] == "continu" and e["duree"]:
            erreurs.append(f"effet {e['id']} : un effet continu n'a pas de durée")


def prix_effet(effet, capacite, cat):
    p = effet["prix"]
    n = capacite.get("n", 0)
    prix_mot_cle = cat["mot-cle"][capacite["mot_cle_donne"]]["prix"] if effet["mot_cle"] else 0
    return (p["par_n"] * n + p["fixe"] + p["par_prix_mot_cle"] * prix_mot_cle) / p["diviseur"]


def facteur_filtre(filtre, cat):
    if not filtre:
        return 1
    cle = next(iter(filtre))
    return cat["filtre"]["carte-liee" if cle == "carte" else cle]["facteur"]


def controler_capacite(capacite, type_carte, cat):
    problemes = []
    if "mot_cle" in capacite:
        mot = cat["mot-cle"].get(capacite["mot_cle"])
        if mot is None:
            return [f"mot-clé inconnu {capacite['mot_cle']}"]
        if type_carte and type_carte not in mot["types"]:
            problemes.append(f"mot-clé {mot['id']} interdit sur {type_carte}")
        return problemes
    effet = cat["effet"].get(capacite["effet"])
    if effet is None:
        return [f"effet inconnu {capacite['effet']}"]
    if capacite["cible"] not in effet["cibles"]:
        problemes.append(f"cible {capacite['cible']} interdite pour {effet['id']}")
    if effet["n"]:
        n = capacite.get("n")
        if n is None or not effet["n"]["min"] <= n <= effet["n"]["max"]:
            problemes.append(f"n hors limites pour {effet['id']}")
    if effet["mot_cle"] and capacite.get("mot_cle_donne") not in cat["mot-cle"]:
        problemes.append(f"mot_cle_donne manquant ou inconnu pour {effet['id']}")
    declencheur = cat["declencheur"].get(capacite.get("declencheur"))
    if effet["sorte"] == "ponctuel" and declencheur is None:
        problemes.append(f"effet ponctuel {effet['id']} sans déclencheur connu")
    if effet["sorte"] == "continu" and "declencheur" in capacite:
        problemes.append(f"effet continu {effet['id']} avec un déclencheur")
    if "duree" in capacite and not effet["duree"]:
        problemes.append(f"effet {effet['id']} sans durée possible")
    if type_carte:
        if declencheur and type_carte not in declencheur["types"]:
            problemes.append(f"déclencheur {declencheur['id']} interdit sur {type_carte}")
        if effet["sorte"] == "continu" and type_carte == "evenement":
            problemes.append("un Événement n'a pas d'effet continu")
        if capacite["cible"] == "cette-carte" and type_carte not in effet["cartes_visees"]:
            problemes.append(f"{effet['id']} ne peut pas viser une carte {type_carte}")
    condition = capacite.get("condition")
    if condition and condition["id"] not in cat["condition"]:
        problemes.append(f"condition inconnue {condition['id']}")
    return problemes


def prix_capacite(capacite, cat):
    if "mot_cle" in capacite:
        return cat["mot-cle"][capacite["mot_cle"]]["prix"]
    effet = cat["effet"][capacite["effet"]]
    valeur = prix_effet(effet, capacite, cat)
    if effet["duree"]:
        valeur *= cat["duree"][capacite.get("duree", "tour")]["facteur"]
    valeur *= cat["cible"][capacite["cible"]]["facteur"]
    valeur *= facteur_filtre(capacite.get("filtre"), cat)
    ajout = 0
    if "declencheur" in capacite:
        declencheur = cat["declencheur"][capacite["declencheur"]]
        valeur *= declencheur["facteur"]
        ajout = declencheur["ajout"]
    if "condition" in capacite:
        valeur *= cat["condition"][capacite["condition"]["id"]]["facteur"]
    return max(cat["prix"]["minimum"], math.ceil(round(valeur, 9)) + ajout)


EXEMPLES = [
    ({"declencheur": "a-la-une", "effet": "renfort", "n": 1, "cible": "une"}, 1),
    ({"declencheur": "a-la-une", "effet": "renfort", "n": 1, "cible": "une", "duree": "permanent"}, 3),
    ({"declencheur": "a-la-une", "effet": "ebauche", "cible": "une", "duree": "permanent"}, 3),
    ({"declencheur": "a-la-une", "effet": "annexion", "n": 4, "cible": "une"}, 3),
    ({"declencheur": "a-la-une", "effet": "annexion", "n": 4, "cible": "une", "duree": "permanent"}, 8),
    ({"effet": "bonus-attaque", "n": 1, "cible": "vos-autres", "filtre": {"type": "creature"}}, 3),
    ({"effet": "bonus-attaque", "n": 2, "cible": "cette-carte", "condition": {"id": "terre-natale", "carte": "Q6697"}}, 1),
    ({"declencheur": "debut-de-tour", "effet": "surtension", "n": 1, "cible": "vous"}, 3),
    ({"effet": "mot-cle-donne", "mot_cle_donne": "initiative", "cible": "vos-autres", "filtre": {"famille": "militaire"}}, 3),
    ({"declencheur": "a-la-une", "effet": "gain-mot-cle", "mot_cle_donne": "imblocable", "cible": "une"}, 1),
    ({"declencheur": "posterite", "effet": "degats", "n": 2, "cible": "une"}, 1),
]


def verifier_exemples(cat, erreurs):
    for capacite, attendu in EXEMPLES:
        for p in controler_capacite(capacite, None, cat):
            erreurs.append(f"exemple {capacite} : {p}")
        obtenu = prix_capacite(capacite, cat)
        if obtenu != attendu:
            erreurs.append(f"exemple {capacite} : prix {obtenu}, attendu {attendu}")


def verifier_cartes(chemin, cat, erreurs):
    with open(chemin, encoding="utf-8") as f:
        for numero, ligne in enumerate(f, 1):
            carte = json.loads(ligne)
            for capacite in carte.get("mecaniques", carte.get("attendu", [])):
                for p in controler_capacite(capacite, carte.get("type"), cat):
                    erreurs.append(f"{chemin}:{numero} {carte.get('titre', carte.get('article'))} : {p}")


def main():
    parser = argparse.ArgumentParser(description="Vérifie la config des mécaniques et, en option, des cartes en JSON Lines.")
    parser.add_argument("cartes", nargs="*", help="fichiers JSON Lines de cartes ou d'articles annotés")
    args = parser.parse_args()
    erreurs = []
    valider_schemas(erreurs)
    cat = charger_catalogue()
    verifier_references(cat, erreurs)
    verifier_exemples(cat, erreurs)
    for chemin in args.cartes:
        verifier_cartes(chemin, cat, erreurs)
    for e in erreurs:
        print(e)
    print(f"{len(erreurs)} erreur(s)")
    sys.exit(1 if erreurs else 0)


if __name__ == "__main__":
    main()
