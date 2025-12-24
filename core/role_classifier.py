import re

ROLE_KEYWORDS = [
    "chief minister",
    "prime minister",
    "president",
    "governor",
    "education minister",
    "health minister",
    "finance minister",
    "home minister",
    "minister"
]

DEPARTMENT_MAP = {
    "education": "Minister for School Education",
    "health": "Minister for Health",
    "finance": "Minister of Finance",
    "home": "Minister of Home Affairs"
}

def is_role_question(text: str) -> bool:
    text = text.lower()
    return "minister" in text or any(k in text for k in ROLE_KEYWORDS)

def extract_role(text: str) -> str:
    text = text.lower().replace("who is", "").strip()

    # ---- Chief Minister ----
    if "chief minister" in text:
        place = text.replace("chief minister", "").strip()
        return f"Chief Minister of {place.title()}"

    # ---- Department Ministers ----
    for dept, title in DEPARTMENT_MAP.items():
        if dept in text and "minister" in text:
            place = text.replace(dept, "").replace("minister", "").strip()
            return f"{title} of {place.title()}"

    # ---- Generic Minister ----
    if "minister" in text:
        place = text.replace("minister", "").strip()
        return f"Minister of {place.title()}"

    return text.title()
