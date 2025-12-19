from core.brain import parse_command
from core.executor import write_file, read_file, delete_file
from core.memory import set_name, get_name
from core.voice import listen
from core.speaker import speak

print("Omni v0.10.7 online.")
print("You can speak or type naturally. Say 'exit' to quit.")

def say(text: str):
    print("Omni:", text)
    speak(text)

while True:
    # Try voice first
    spoken = listen()

    if spoken:
        print(f"You (voice): {spoken}")
        user_input = spoken.strip()
    else:
        user_input = input("You: ").strip()

    if not user_input:
        continue

    intent_data = parse_command(user_input)
    intent = intent_data.get("intent")

    # EXIT
    if intent == "exit":
        say("Goodbye.")
        break

    # GREETING
    elif intent == "greet":
        name = get_name()
        if name:
            say(f"Hello {name}")
        else:
            say("Hello")

    # ASK NAME (INCOMPLETE)
    elif intent == "ask_name":
        say("Please tell me your name.")

    # SET NAME
    elif intent == "set_name":
        set_name(intent_data["name"])
        say(f"Nice to meet you, {intent_data['name']}.")

    # GET NAME
    elif intent == "get_name":
        name = get_name()
        if name:
            say(f"Your name is {name}.")
        else:
            say("I don't know your name yet.")

    # EXPLAIN MEMORY
    elif intent == "explain_name":
        name = get_name()
        if name:
            say("You told me your name earlier, so I remembered it.")
        else:
            say("You have not told me your name yet.")

    # WRITE FILE
    elif intent == "write_file":
        ok, msg = write_file(
            intent_data["path"],
            intent_data["content"]
        )
        say(msg)

    # READ FILE
    elif intent == "read_file":
        ok, result = read_file(intent_data["path"])
        if ok:
            say(result)
        else:
            say("File not found.")

    # DELETE FILE
    elif intent == "delete_file":
        ok, msg = delete_file(intent_data["path"])
        say(msg)

    # WAIT (IGNORE SILENCE)
    elif intent == "wait":
        continue

    # UNKNOWN
    else:
        say("I am still learning.")
