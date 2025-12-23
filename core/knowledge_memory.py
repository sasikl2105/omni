import json
import os
import time

KNOWLEDGE_PATH = os.path.expanduser(
    "~/omni/data/memory/knowledge.json"
)

def _load():
    if not os.path.exists(KNOWLEDGE_PATH):
        return {}
    with open(KNOWLEDGE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def _save(data):
    with open(KNOWLEDGE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def remember_fact(topic, content, source="self"):
    data = _load()
    data[topic.lower()] = {
        "content": content,
        "source": source,
        "learned_at": time.time()
    }
    _save(data)

def recall_fact(topic):
    data = _load()
    return data.get(topic.lower())
