import os
import json

AIS_DIR = os.path.expanduser("~/omni/ais")

def list_ais():
    if not os.path.exists(AIS_DIR):
        return []

    return [
        d for d in os.listdir(AIS_DIR)
        if os.path.isdir(os.path.join(AIS_DIR, d))
    ]

def load_ai_config(name):
    path = os.path.join(AIS_DIR, name, "config.json")
    if not os.path.exists(path):
        return None

    with open(path, "r") as f:
        return json.load(f)
