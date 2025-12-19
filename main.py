from core.brain import parse_command
from core.executor import write_file, read_file, delete_file
from core.memory import set_name, get_name

print("Omni v0.10.2 online. Say hi 👋")

while True:
    user_input = input("You: ").strip()

    intent_data = parse_command(user_input)
    intent = intent_data.get("intent")

    if intent == "exit":
        print("Omni: Goodbye. Shutting down.")
        break

    elif intent == "greet":
        name = get_name()
        if name:
            print(f"Omni: Hello {name} 👋")
        else:
            print("Omni: Hello 👋")

    elif intent == "set_name":
        set_name(intent_data["name"])
        print(f"Omni: Nice to meet you, {intent_data['name']}.")

    elif intent == "get_name":
        name = get_name()
        if name:
            print(f"Omni: Your name is {name}.")
        else:
            print("Omni: I don't know your name yet.")

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
