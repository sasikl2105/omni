import json, os
BASE = os.path.dirname(os.path.dirname(__file__))
FILE = os.path.join(BASE, "data", "persistent_memory.json")

DEFAULT = {"user": {}, "preferences": {}, "facts": {}}

def load():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return DEFAULT.copy()

def save(mem):
    with open(FILE, "w") as f:
        json.dump(mem, f, indent=2)

def get(path, default=None):
    mem = load()
    for k in path.split("."):
        if not isinstance(mem, dict):
            return default
        mem = mem.get(k)
        if mem is None:
            return default
    return mem

def set(path, value):
    mem = load()
    ref = mem
    keys = path.split(".")
    for k in keys[:-1]:
        ref = ref.setdefault(k, {})
    ref[keys[-1]] = value
    save(mem)
