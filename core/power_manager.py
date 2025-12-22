import json
import os

AI_ROOT = os.path.expanduser("~/omni/ais")


def ai_path(name):
    return os.path.join(AI_ROOT, name)


def config_path(name):
    return os.path.join(ai_path(name), "config.json")


def grant_powers(name, abilities=None, permissions=None):
    path = ai_path(name)
    if not os.path.isdir(path):
        return f"AI '{name}' does not exist."

    config = {
        "name": name,
        "abilities": abilities or [],
        "permissions": permissions or [],
        "locked": True
    }

    with open(config_path(name), "w") as f:
        json.dump(config, f, indent=2)

    return f"Powers granted to AI '{name}'."
