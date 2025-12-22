import json
import os
from datetime import datetime

MEMORY_DIR = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "memory"
)

os.makedirs(MEMORY_DIR, exist_ok=True)


def _memory_path(ai_name):
    return os.path.join(MEMORY_DIR, f"{ai_name}.json")


def load_memory(ai_name):
    path = _memory_path(ai_name)
    if not os.path.exists(path):
        return []

    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception:
        return []


def save_memory(ai_name, memory):
    path = _memory_path(ai_name)
    with open(path, "w") as f:
        json.dump(memory, f, indent=2)


def remember(ai_name, role, content):
    memory = load_memory(ai_name)

    memory.append({
        "time": datetime.now().isoformat(),
        "role": role,
        "content": content
    })

    save_memory(ai_name, memory)


def recall(ai_name, limit=5):
    memory = load_memory(ai_name)
    return memory[-limit:]
