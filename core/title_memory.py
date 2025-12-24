import json
import os
import time

TITLE_PATH = os.path.expanduser(
    "~/omni/data/memory/titles.json"
)

def _load():
    if not os.path.exists(TITLE_PATH):
        return {}
    with open(TITLE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def _save(data):
    os.makedirs(os.path.dirname(TITLE_PATH), exist_ok=True)
    with open(TITLE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

# =========================
# PUBLIC API
# =========================

def get_title(title: str):
    """
    Returns learned title mapping if exists
    """
    data = _load()
    return data.get(title.lower())

def remember_title(title: str, person: str, confidence: float = 0.6):
    """
    Store a learned title with confidence score
    """
    data = _load()

    title = title.lower()
    person = person.lower()

    if title in data:
        # increase confidence slowly
        data[title]["confidence"] = min(
            1.0, data[title]["confidence"] + 0.1
        )
    else:
        data[title] = {
            "person": person,
            "confidence": confidence,
            "learned_at": time.time()
        }

    _save(data)
