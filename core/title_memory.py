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
    data = _load()
    return data.get(title.lower())

def remember_title(title: str, person: str, confidence=0.5):
    data = _load()

    title = title.lower()
    person = person.lower()

    if title in data:
        data[title]["confidence"] = min(
            1.0, data[title]["confidence"] + 0.1
        )
        data[title]["person"] = person
    else:
        data[title] = {
            "person": person,
            "confidence": confidence,
            "learned_at": time.time()
        }

    _save(data)
