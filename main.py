from core.brain import parse_command
from core.executor import write_file, read_file, delete_file

print("Omni v0.10.1 online. Type 'bye' or 'exit' to quit.")

while True:
    user_input = input("You: ").strip()

    intent_data = parse_command(user_input)
    intent = intent_data.get("intent")

    if intent == "exit":
        print("Omni: Goodbye. Shutting down.")
        break

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
        print("Omni: I did not understand that yet.")
