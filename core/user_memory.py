# core/user_memory.py

import json
import os

PATH = os.path.expanduser("~/omni/data/user_profile.json")

def load():
    if not os.path.exists(PATH):
        return {}
    with open(PATH, "r") as f:
        return json.load(f)

def save(data):
    os.makedirs(os.path.dirname(PATH), exist_ok=True)
    with open(PATH, "w") as f:
        json.dump(data, f, indent=2)

def remember(key, value):
    data = load()
    data[key] = value
    save(data)

def forget(key):
    data = load()
    if key in data:
        del data[key]
        save(data)

def recall(key):
    return load().get(key)
