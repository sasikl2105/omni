from core.brain import parse_command
from core.executor import write_file, read_file, delete_file
from core.memory import set_name, get_name
from core.voice import listen

print("Omni v0.10.4 online.")
print("Choose input mode each time.")

while True:
    print("\n[V] Voice  |  [T] Type  |  [Q] Quit")
    mode = input("Mode: ").strip().lower()

    if mode == "q":
        print("Omni: Goodbye.")
        break

    if mode == "v":
        print("[Listening...] Speak now")
        spoken = listen()

        if not spoken or not spoken.strip():
            print("Omni: I didn't hear anything.")
            continue

        print(f"You (voice): {spoken}")
        user_input = spoken.strip()

    elif mode == "t":
        user_input = input("You: ").strip()
        if not user_input:
            continue

    else:
        print("Omni: Invalid option.")
        continue

    intent_data = parse_command(user_input)
    intent = intent_data.get("intent")

    if intent == "exit":
        print("Omni: Goodbye.")
        break

    elif intent == "greet":
        name = get_name()
        print(f"Omni: Hello {name} 👋" if name else "Omni: Hello 👋")

    elif intent == "ask_name":
        print("Omni: Please tell me your name.")

    elif intent == "set_name":
        set_name(intent_data["name"])
        print(f"Omni: Nice to meet you, {intent_data['name']}.")

    elif intent == "get_name":
        name = get_name()
        print(f"Omni: Your name is {name}." if name else "Omni: I don't know your name yet.")

    elif intent == "write_file":
        ok, msg = write_file(
            intent_data["path"],
            intent_data["content"]
        )
        print("Omni:", msg)

    elif intent == "read_file":
        ok, result = read_file(intent_data["path"])
        print("Omni:", result)

    elif intent == "delete_file":
        ok, msg = delete_file(intent_data["path"])
        print("Omni:", msg)

    else:
        print("Omni: I am still learning.")
