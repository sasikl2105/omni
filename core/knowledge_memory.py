import json
import os
from datetime import datetime

MEMORY_FILE = os.path.expanduser("~/omni/data/memory/knowledge.json")

def _load():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def _save(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def recall(question: str):
    data = _load()
    return data.get(question.lower())

def remember(question: str, answer: str, source="web"):
    data = _load()
    data[question.lower()] = {
        "answer": answer,
        "source": source,
        "learned_at": datetime.utcnow().isoformat()
    }
    _save(data)
