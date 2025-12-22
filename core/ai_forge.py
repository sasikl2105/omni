import os
import json
from datetime import datetime

AIS_DIR = "ais"


def create_ai(name, abilities, permissions=None):
    name = name.lower()
    ai_path = os.path.join(AIS_DIR, name)

    if os.path.exists(ai_path):
        return f"AI '{name}' already exists."

    os.makedirs(ai_path, exist_ok=True)

    rules = {
        "name": name.capitalize(),
        "created_by": "Jarvis",
        "created_at": datetime.utcnow().isoformat(),
        "abilities": abilities,
        "permissions": permissions or [],
        "restrictions": [
            "no_self_modify",
            "no_network_access"
        ]
    }

    with open(os.path.join(ai_path, "rules.json"), "w") as f:
        json.dump(rules, f, indent=2)

    brain_code = f'''import json

def load_rules():
    with open("rules.json") as f:
        return json.load(f)

def respond(text):
    rules = load_rules()
    abilities = ", ".join(rules["abilities"])
    return f"I am {{rules['name']}}, created by Jarvis. My abilities: {{abilities}}."

if __name__ == "__main__":
    rules = load_rules()
    print(f"{{rules['name']}} online.")
    while True:
        text = input("> ")
        if text.lower() in ("exit", "quit"):
            break
        print(respond(text))
'''

    with open(os.path.join(ai_path, "main.py"), "w") as f:
        f.write(brain_code)

    return f"AI '{name}' created successfully."
