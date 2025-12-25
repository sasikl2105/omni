# core/role_classifier.py
# Strict role classification for OMNI (with grammar normalization)

ROLE_KEYWORDS = [
    "president",
    "prime minister",
    "chief minister",
    "education minister",
    "health minister",
    "finance minister",
    "home minister",
    "minister"
]

def is_role_question(text: str) -> bool:
    text = text.lower()
    return text.startswith("who is") and any(k in text for k in ROLE_KEYWORDS)


def extract_role(text: str) -> str | None:
    """
    Normalize role questions:
    - who is president of india
    - who is india president
    """

    text = text.lower().replace("who is", "").strip()

    # Case 1: correct form
    if " of " in text:
        return text

    # Case 2: reversed form → "america president"
    parts = text.split()
    if len(parts) >= 2 and parts[-1] in ROLE_KEYWORDS:
        country = " ".join(parts[:-1])
        role = parts[-1]
        return f"{role} of {country}"

    return None
