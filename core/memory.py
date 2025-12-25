# core/memory.py
# Safe persistent memory handler

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MEMORY_FILE = os.path.join(BASE_DIR, "data", "memory.json")

DEFAULT_MEMORY = {
    "user": {}
}

def _load():
    if not os.path.exists(MEMORY_FILE):
        _save(DEFAULT_MEMORY)
        return DEFAULT_MEMORY.copy()

    try:
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)
            if not isinstance(data, dict):
                raise ValueError
            return data
    except Exception:
        # Auto-heal corrupted memory
        _save(DEFAULT_MEMORY)
        return DEFAULT_MEMORY.copy()

def _save(mem):
    with open(MEMORY_FILE, "w") as f:
        json.dump(mem, f, indent=2)

def set_name(name: str):
    mem = _load()
    mem.setdefault("user", {})
    mem["user"]["name"] = name
    _save(mem)

def get_name():
    mem = _load()
    return mem.get("user", {}).get("name")

# ===============================
# USER PREFERENCES (SAFE DEFAULT)
# ===============================

def get_pref(key, default=None):
    return default
