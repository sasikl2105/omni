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
    intent = data.get("intent")

    # exit
    if intent == "exit":
        print("Omni: Goodbye.")
        break

    # greeting
    elif intent == "greet":
        name = get_name()
        if name:
            print(f"Omni: Hello {name}")
        else:
            print("Omni: Hello 👋")

    # explain memory
    elif intent == "explain_name":
        name = get_name()
        if name:
            print("Omni: You told me your name earlier, so I remembered it.")
        else:
            print("Omni: You haven't told me your name yet.")

    # set name
    elif intent == "set_name":
        set_name(data["name"])
        print(f"Omni: Nice to meet you, {data['name']}.")

    # get name
    elif intent == "get_name":
        print("Omni:", get_name() or "I don't know yet.")

    # ethical hacking assistant
    elif intent == "studentbae":
        print("\nOmni:", studentbae(text), "\n")

    # glitchwood assistant
    elif intent == "glitchwood":
        if require_permission():
            print("Omni:", create_player())

    # root command (safe / simulated)
    elif intent == "root":
        if require_permission():
            print("Omni:", run_root(data.get("cmd")))

    # battery info
    elif intent == "battery":
        print("Omni:", battery_status())

    # fallback
    else:
        print("Omni: I am still learning.")
