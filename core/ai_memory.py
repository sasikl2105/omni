import json
import os
import time

MEMORY_DIR = os.path.expanduser("~/omni/data/memory")

os.makedirs(MEMORY_DIR, exist_ok=True)


def _path(name):
    return os.path.join(MEMORY_DIR, f"{name}.json")


def load_memory(name):
    path = _path(name)
    if not os.path.exists(path):
        return []

    with open(path, "r") as f:
        return json.load(f)


def save_event(name, event):
    memory = load_memory(name)

    memory.append({
        "time": time.time(),
        "event": event
    })

    with open(_path(name), "w") as f:
        json.dump(memory, f, indent=2)


def recall(name, limit=5):
    memory = load_memory(name)
    return memory[-limit:]
