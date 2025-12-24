import json
import os
import time

TITLE_MEMORY_PATH = os.path.expanduser(
    "~/omni/data/memory/titles.json"
)

def _load():
    if not os.path.exists(TITLE_MEMORY_PATH):
        return {}
    with open(TITLE_MEMORY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def _save(data):
    os.makedirs(os.path.dirname(TITLE_MEMORY_PATH), exist_ok=True)
    with open(TITLE_MEMORY_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def remember_title(title, entity, source="unknown", confidence=0.5):
    data = _load()
    data[title.lower()] = {
        "entity": entity,
        "confidence": confidence,
        "source": source,
        "learned_at": time.time()
    }
    _save(data)

def recall_title(title):
    data = _load()
    return data.get(title.lower())
