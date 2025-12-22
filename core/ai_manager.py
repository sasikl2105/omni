import json
import os

AIS_DIR = os.path.expanduser("~/omni/ais")


def ai_path(name):
    return os.path.join(AIS_DIR, name)


def config_path(name):
    return os.path.join(ai_path(name), "config.json")


def load_config(name):
    path = config_path(name)
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        return json.load(f)


def save_config(name, config):
    with open(config_path(name), "w") as f:
        json.dump(config, f, indent=2)


def unlock_ai(name, abilities=None, permissions=None):
    config = load_config(name)
    if not config:
        return False, "AI does not exist."

    if abilities:
        config["abilities"] = list(set(config.get("abilities", []) + abilities))

    if permissions:
        config["permissions"] = list(set(config.get("permissions", []) + permissions))

    config["locked"] = False
    save_config(name, config)
    return True, f"AI '{name}' unlocked and activated."
