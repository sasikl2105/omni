from core.brain import parse
from core.memory import get_name, set_name
from core.security import require_permission
from core.system_access import battery_status
from core.root_access import run_root
from plugins.studentbae import handle as studentbae
from plugins.glitchwood import create_player

print("Omni online. Type 'exit' to quit.")

while True:
    text = input("You: ").strip()
    if not text:
        continue

    data = parse(text)
    intent = data["intent"]

    if intent == "exit":
        print("Omni: Goodbye.")
        break

    if intent == "set_name":
        set_name(data["name"])
        print(f"Omni: Nice to meet you, {data['name']}.")
        continue

    if intent == "get_name":
        print("Omni:", get_name() or "I don't know yet.")
        continue

    if intent == "studentbae":
        print("\nOmni:", studentbae(text), "\n")
        continue

    if intent == "glitchwood":
        if require_permission():
            print("Omni:", create_player())
        continue

    if intent == "root":
        print("Omni:", run_root(data["cmd"]))
        continue

    if "battery" in text:
        print("Omni:", battery_status())
        continue

    print("Omni: I am still learning.")
