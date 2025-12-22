import os
import json

BASE_DIR = os.path.expanduser("~/omni/ais")


def _ai_path(name):
    return os.path.join(BASE_DIR, name)


def create_ai(name, abilities="", permissions=""):
    name = name.lower().strip()
    path = _ai_path(name)

    if os.path.exists(path):
        return f"AI '{name}' already exists."

    os.makedirs(path, exist_ok=True)

    config = {
        "name": name,
        "abilities": [a.strip() for a in abilities.split(",") if a.strip()],
        "permissions": [p.strip() for p in permissions.split(",") if p.strip()],
        "locked": True
    }

    with open(os.path.join(path, "config.json"), "w") as f:
        json.dump(config, f, indent=2)

    # Minimal AI main.py
    with open(os.path.join(path, "main.py"), "w") as f:
        f.write(f'''import json

with open("config.json") as f:
    config = json.load(f)

print("{name.capitalize()} online.")

while True:
    text = input("> ").strip()
    if text == "exit":
        break

    if config.get("locked"):
        print("I am restricted and cannot respond.")
        continue

    print(f"I am {name.capitalize()}, created by Jarvis. My abilities: {{', '.join(config['abilities'])}}.")
''')

    return f"AI '{name}' created and locked."


def grant_powers(name, abilities="", permissions=""):
    name = name.lower().strip()
    path = _ai_path(name)

    if not os.path.exists(path):
        return f"AI '{name}' does not exist."

    config_path = os.path.join(path, "config.json")
    if not os.path.exists(config_path):
        return f"AI '{name}' config missing."

    with open(config_path) as f:
        config = json.load(f)

    new_abilities = [a.strip() for a in abilities.split(",") if a.strip()]
    new_permissions = [p.strip() for p in permissions.split(",") if p.strip()]

    config["abilities"] = list(set(config["abilities"] + new_abilities))
    config["permissions"] = list(set(config["permissions"] + new_permissions))
    config["locked"] = False

    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)

    return f"AI '{name}' unlocked and activated."
