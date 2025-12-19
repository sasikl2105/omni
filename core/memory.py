import json
import os

MEMORY_FILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "memory.json"
)

def _load():
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def _save(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def set_name(name: str):
    data = _load()
    data["name"] = name
    _save(data)

def get_name():
    return _load().get("name")
