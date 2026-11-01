VOWELS = "AEIOUYÀÂÉÈÊËÎÏÔÛÙÜaeiouyàâéèêëîïôûùü"
LANGUAGE = "fr"


def card_noun(card_types, type_id):
    return card_types[type_id]["name"][LANGUAGE]


GENERIC_NOUN = {"singular": "carte", "plural": "cartes", "gender": "f"}


def nouns_for(types, card_types):
    permanents = {t for t in card_types if t != "event"}
    if not types or set(types) >= permanents:
        return [GENERIC_NOUN]
    return [card_noun(card_types, t) for t in card_types if t in types]


def determiner_a(noun):
    return "une" if noun["gender"] == "f" else "un"


def determiner_this(noun):
    if noun["gender"] == "f":
        return "cette"
    return "cet" if noun["singular"][0] in VOWELS else "ce"


def determiner_all(noun):
    return "toutes les" if noun["gender"] == "f" else "tous les"


def with_family(word, family):
    return f"{word} {family}" if family else word


def noun_phrase(pattern, number, nouns, family, other=""):
    parts = []
    for noun in nouns:
        part = pattern["each"]
        part = part.replace("{noun}", with_family(noun["singular"], family))
        part = part.replace("{nouns}", with_family(noun["plural"], family))
        part = part.replace("{a}", determiner_a(noun))
        part = part.replace("{this}", determiner_this(noun))
        part = part.replace("{all}", determiner_all(noun))
        parts.append(part)
    joined = (" ou " if number == "singular" else " et ").join(parts)
    return pattern["prefix"].replace("{other}", other) + joined + pattern["suffix"]


def phrase_gender(nouns):
    return "f" if all(n["gender"] == "f" for n in nouns) else "m"


def filter_parts(card_filter):
    card_filter = card_filter or {}
    return card_filter.get("type"), card_filter.get("family"), card_filter.get("card")


def subject_phrase(card_filter, catalogue, card_types, labels):
    filter_type, family, card = filter_parts(card_filter)
    if card:
        return labels.get(card, card), "m"
    nouns = nouns_for([filter_type] if filter_type else None, card_types)
    pattern = catalogue["target"]["one"]["text"][LANGUAGE]
    return noun_phrase(pattern, "singular", nouns, family), phrase_gender(nouns)


FIXED_GENDER = {"equipped": "f"}


def target_types(mechanic, effect, bearer_type, catalogue):
    filter_type, _, _ = filter_parts(mechanic.get("filter"))
    if mechanic["target"] == "self" and bearer_type:
        return [bearer_type]
    if filter_type:
        return [filter_type]
    types = effect["affected_types"]
    keyword = mechanic.get("granted_keyword")
    if keyword:
        types = [t for t in types if t in catalogue["keyword"][keyword]["types"]]
    return types


def target_phrase(mechanic, effect, bearer_type, catalogue, card_types, labels):
    target = catalogue["target"][mechanic["target"]]
    pattern = target["text"][LANGUAGE]
    if "{noun" not in pattern["each"]:
        return pattern["prefix"] + pattern["each"] + pattern["suffix"], FIXED_GENDER.get(mechanic["target"], "m")
    _, family, card = filter_parts(mechanic.get("filter"))
    if card:
        return labels.get(card, card), "m"
    types = target_types(mechanic, effect, bearer_type, catalogue)
    nouns = nouns_for(types, card_types)
    other = "autres " if bearer_type is None or bearer_type in types or nouns == [GENERIC_NOUN] else ""
    return noun_phrase(pattern, target["number"], nouns, family, other), phrase_gender(nouns)


def fill(text, values):
    for key, value in values.items():
        text = text.replace("{" + key + "}", str(value))
    return text


def effect_text(mechanic, bearer_type, catalogue, card_types, labels):
    effect = catalogue["effect"][mechanic["effect"]]
    number = catalogue["target"][mechanic["target"]]["number"]
    n = mechanic.get("n", 0)
    keyword = mechanic.get("granted_keyword")
    phrase, gender = target_phrase(mechanic, effect, bearer_type, catalogue, card_types, labels)
    text = fill(effect["text"][LANGUAGE][number], {
        "target": phrase,
        "e": "e" if gender == "f" else "",
        "n": n,
        "s": "s" if n > 1 else "",
        "keyword": catalogue["keyword"][keyword]["name"][LANGUAGE] if keyword else "",
    })
    if effect["has_duration"]:
        duration_id = mechanic.get("duration", "turn")
        duration = effect.get("duration_text", {}).get(duration_id) or catalogue["duration"][duration_id]["text"]
        duration_words = duration[LANGUAGE][number]
        if duration_words:
            text = f"{text} {duration_words}"
    return text


def trigger_text(mechanic, catalogue, card_types, labels):
    trigger = catalogue["trigger"][mechanic["trigger"]]
    subject, gender = subject_phrase(mechanic.get("trigger_filter"), catalogue, card_types, labels)
    return fill(trigger["text"][LANGUAGE], {
        "n": mechanic.get("trigger_n", 0),
        "subject": subject,
        "e": "e" if gender == "f" else "",
    })


def condition_text(condition, triggered, catalogue, card_types, labels):
    template = catalogue["condition"][condition["id"]]["text"][LANGUAGE]
    subject, _ = subject_phrase(condition.get("filter"), catalogue, card_types, labels)
    card = condition.get("card")
    return fill(template, {
        "conj": "si" if triggered else "tant que",
        "subject": subject,
        "card": labels.get(card, card) if card else "",
        "n": condition.get("n", 0),
    })


ELISIONS = [(" de une ", " d'une "), (" de un ", " d'un "), (" que il", " qu'il"), (" que elle", " qu'elle")]


def elide(text):
    for full, short in ELISIONS:
        text = text.replace(full, short)
    return text


def capitalize(text):
    return text[:1].upper() + text[1:]


def render(mechanic, bearer_type, catalogue, card_types, labels=None, detailed=False):
    labels = labels or {}
    if "keyword" in mechanic:
        keyword = catalogue["keyword"][mechanic["keyword"]]
        name = keyword["name"][LANGUAGE]
        return f"{name} : {keyword['text'][LANGUAGE]}" if detailed else name
    body = effect_text(mechanic, bearer_type, catalogue, card_types, labels)
    triggered = "trigger" in mechanic
    if "condition" in mechanic:
        body = f"{condition_text(mechanic['condition'], triggered, catalogue, card_types, labels)}, {body}"
    if triggered:
        return elide(f"{trigger_text(mechanic, catalogue, card_types, labels)} : {body}.")
    return elide(f"{capitalize(body)}.")
