import argparse
import json
import math
import os
import pathlib
import sys

import jsonschema
from referencing import Registry, Resource

CONFIG_ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "config"))
CONFIG_DIR = os.path.join(CONFIG_ROOT, "mechanics")
CARD_TYPE_FILE = os.path.join(CONFIG_ROOT, "card", "type.json")
CATALOGUE_FILES = {
    "keyword": "keywords",
    "trigger": "triggers",
    "effect": "effects",
    "duration": "durations",
    "target": "targets",
    "filter": "filters",
    "condition": "conditions",
}


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def schema_uri(path):
    return pathlib.Path(path).resolve().as_uri()


def load_schema(path):
    return {**load_json(path), "$id": schema_uri(path)}


def schema_registry():
    resources = []
    for directory, _, names in os.walk(CONFIG_ROOT):
        for name in names:
            if name.endswith(".schema.json"):
                path = os.path.join(directory, name)
                resources.append((schema_uri(path), Resource.from_contents(load_schema(path))))
    return Registry().with_resources(resources)


def validator_for(schema_path, registry):
    return jsonschema.Draft202012Validator(load_schema(schema_path), registry=registry)


def schema_path_for(config_path):
    directory, name = os.path.split(config_path)
    return os.path.join(directory, "schema", name.replace(".json", ".schema.json"))


def validate_config(registry, errors):
    paths = [os.path.join(CONFIG_DIR, f"{name}.json") for name in list(CATALOGUE_FILES) + ["cost"]] + [CARD_TYPE_FILE]
    for path in paths:
        for error in validator_for(schema_path_for(path), registry).iter_errors(load_json(path)):
            errors.append(f"{os.path.relpath(path, CONFIG_ROOT)}: {error.message}")


def check_card_types(errors):
    listed = [t["id"] for t in load_json(CARD_TYPE_FILE)["types"]]
    allowed = load_json(schema_path_for(CARD_TYPE_FILE))["$defs"]["card_type"]["enum"]
    if sorted(listed) != sorted(allowed):
        errors.append(f"card/type.json lists {listed}, schema allows {allowed}")


def load_catalogue():
    catalogue = {
        name: {item["id"]: item for item in load_json(os.path.join(CONFIG_DIR, f"{name}.json"))[key]}
        for name, key in CATALOGUE_FILES.items()
    }
    catalogue["cost"] = load_json(os.path.join(CONFIG_DIR, "cost.json"))
    return catalogue


def check_references(catalogue, errors):
    for effect in catalogue["effect"].values():
        for target in effect["targets"]:
            if target not in catalogue["target"]:
                errors.append(f"effect {effect['id']}: unknown target {target}")
        if effect["kind"] == "static" and effect["has_duration"]:
            errors.append(f"effect {effect['id']}: a static effect has no duration")


def effect_base_cost(effect, mechanic, catalogue):
    cost = effect["cost"]
    keyword_cost = catalogue["keyword"][mechanic["granted_keyword"]]["cost"] if effect["takes_keyword"] else 0
    return (cost["per_n"] * mechanic.get("n", 0) + cost["flat"] + cost["per_keyword_cost"] * keyword_cost) / cost["divisor"]


def filter_factor(card_filter, catalogue):
    if not card_filter:
        return 1
    key = next(iter(card_filter))
    return catalogue["filter"]["linked-card" if key == "card" else key]["factor"]


def check_mechanic(mechanic, card_type, catalogue):
    problems = []
    if "keyword" in mechanic:
        keyword = catalogue["keyword"].get(mechanic["keyword"])
        if keyword is None:
            return [f"unknown keyword {mechanic['keyword']}"]
        if card_type and card_type not in keyword["types"]:
            problems.append(f"keyword {keyword['id']} not allowed on {card_type}")
        return problems
    effect = catalogue["effect"].get(mechanic["effect"])
    if effect is None:
        return [f"unknown effect {mechanic['effect']}"]
    if mechanic["target"] not in effect["targets"]:
        problems.append(f"target {mechanic['target']} not allowed for {effect['id']}")
    if effect["n"]:
        n = mechanic.get("n")
        if n is None or not effect["n"]["min"] <= n <= effect["n"]["max"]:
            problems.append(f"n out of range for {effect['id']}")
    if effect["takes_keyword"] and mechanic.get("granted_keyword") not in catalogue["keyword"]:
        problems.append(f"missing or unknown granted_keyword for {effect['id']}")
    trigger = catalogue["trigger"].get(mechanic.get("trigger"))
    if effect["kind"] == "triggered" and trigger is None:
        problems.append(f"triggered effect {effect['id']} without a known trigger")
    if effect["kind"] == "static" and "trigger" in mechanic:
        problems.append(f"static effect {effect['id']} with a trigger")
    if "duration" in mechanic and not effect["has_duration"]:
        problems.append(f"effect {effect['id']} takes no duration")
    if card_type:
        if trigger and card_type not in trigger["types"]:
            problems.append(f"trigger {trigger['id']} not allowed on {card_type}")
        if effect["kind"] == "static" and card_type == "event":
            problems.append("an event has no static effect")
        if mechanic["target"] == "self" and card_type not in effect["affected_types"]:
            problems.append(f"{effect['id']} cannot affect cards of type {card_type}")
    condition = mechanic.get("condition")
    if condition and condition["id"] not in catalogue["condition"]:
        problems.append(f"unknown condition {condition['id']}")
    return problems


def mechanic_cost(mechanic, catalogue):
    if "keyword" in mechanic:
        return catalogue["keyword"][mechanic["keyword"]]["cost"]
    effect = catalogue["effect"][mechanic["effect"]]
    value = effect_base_cost(effect, mechanic, catalogue)
    if effect["has_duration"]:
        value *= catalogue["duration"][mechanic.get("duration", "turn")]["factor"]
    value *= catalogue["target"][mechanic["target"]]["factor"]
    value *= filter_factor(mechanic.get("filter"), catalogue)
    offset = 0
    if "trigger" in mechanic:
        trigger = catalogue["trigger"][mechanic["trigger"]]
        value *= trigger["factor"]
        offset = trigger["offset"]
    if "condition" in mechanic:
        value *= catalogue["condition"][mechanic["condition"]["id"]]["factor"]
    return max(catalogue["cost"]["minimum"], math.ceil(round(value, 9)) + offset)


DOCUMENTED_EXAMPLES = [
    ({"trigger": "on-play", "effect": "pump", "n": 1, "target": "one"}, 1),
    ({"trigger": "on-play", "effect": "pump", "n": 1, "target": "one", "duration": "permanent"}, 3),
    ({"trigger": "on-play", "effect": "stub", "target": "one", "duration": "permanent"}, 3),
    ({"trigger": "on-play", "effect": "steal", "n": 4, "target": "one"}, 3),
    ({"trigger": "on-play", "effect": "steal", "n": 4, "target": "one", "duration": "permanent"}, 8),
    ({"effect": "attack-bonus", "n": 1, "target": "your-others", "filter": {"type": "creature"}}, 3),
    ({"effect": "attack-bonus", "n": 2, "target": "self", "condition": {"id": "birthplace", "card": "Q6697"}}, 1),
    ({"trigger": "turn-start", "effect": "surge", "n": 1, "target": "you"}, 3),
    ({"effect": "keyword-aura", "granted_keyword": "first-strike", "target": "your-others", "filter": {"family": "militaire"}}, 3),
    ({"trigger": "on-play", "effect": "grant-keyword", "granted_keyword": "unblockable", "target": "one"}, 1),
    ({"trigger": "on-death", "effect": "damage", "n": 2, "target": "one"}, 1),
]


def check_documented_examples(catalogue, errors):
    for mechanic, expected in DOCUMENTED_EXAMPLES:
        for problem in check_mechanic(mechanic, None, catalogue):
            errors.append(f"example {mechanic}: {problem}")
        cost = mechanic_cost(mechanic, catalogue)
        if cost != expected:
            errors.append(f"example {mechanic}: cost {cost}, expected {expected}")


def check_cards(path, catalogue, card_validator, errors):
    with open(path, encoding="utf-8") as f:
        for line_number, line in enumerate(f, 1):
            card = json.loads(line)
            label = f"{path}:{line_number} {card.get('title', card.get('article'))}"
            for error in card_validator.iter_errors({"article": card["article"], "mechanics": card.get("mechanics", [])}):
                errors.append(f"{label}: {error.message}")
            for mechanic in card.get("mechanics", []):
                for problem in check_mechanic(mechanic, card.get("type"), catalogue):
                    errors.append(f"{label}: {problem}")


def main():
    parser = argparse.ArgumentParser(description="Check the mechanics config and, optionally, cards in JSON Lines.")
    parser.add_argument("cards", nargs="*", help="JSON Lines files of cards with a mechanics list")
    args = parser.parse_args()
    errors = []
    registry = schema_registry()
    validate_config(registry, errors)
    catalogue = load_catalogue()
    check_references(catalogue, errors)
    check_documented_examples(catalogue, errors)
    check_card_types(errors)
    card_validator = validator_for(os.path.join(CONFIG_DIR, "schema", "card-mechanics.schema.json"), registry)
    for path in args.cards:
        check_cards(path, catalogue, card_validator, errors)
    for error in errors:
        print(error)
    print(f"{len(errors)} error(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
