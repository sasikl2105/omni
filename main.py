from core.brain import parse_command
from core.executor import write_file, read_file, delete_file
from core.memory import set_name, get_name
from core.voice import listen
from core.speaker import speak
from core.context import set_context, get_context

print("Omni v0.12.2 online.")

def say(text: str):
    print("Omni:", text)
    speak(text)

# ---------- INPUT MODE SETUP ----------
input_mode = None

while input_mode not in ["voice", "text"]:
    choice = input("Choose input mode (voice/text): ").strip().lower()
    if choice in ["voice", "text"]:
        input_mode = choice
    else:
        print("Please type 'voice' or 'text'.")

say(f"{input_mode.capitalize()} mode activated.")
print("Say 'switch to voice mode' or 'switch to text mode' anytime.")
print("Say 'exit' or 'bye' to quit.")

# ---------- MAIN LOOP ----------
while True:
    context = get_context()

    # INPUT
    if input_mode == "voice":
        spoken = listen()
        if spoken:
            print(f"You (voice): {spoken}")
            user_input = spoken.strip()
        else:
            user_input = input("You: ").strip()
    else:
        user_input = input("You: ").strip()

    if not user_input:
        continue

    lower_input = user_input.lower()

    # EXIT
    if any(x in lower_input for x in ["exit", "bye", "quit"]):
        say("Goodbye.")
        break

    # MODE SWITCH
    if any(x in lower_input for x in ["switch to voice", "voice mode", "voice on"]):
        input_mode = "voice"
        say("Voice mode activated.")
        continue

    if any(x in lower_input for x in ["switch to text", "text mode", "voice off", "text only"]):
        input_mode = "text"
        say("Text mode activated.")
        continue

    intent_data = parse_command(user_input)
    intent = intent_data.get("intent")

    # CONTEXT FOLLOW-UP
    if "me" in lower_input and context["last_entity"]:
        say(f"You are {context['last_entity']}.")
        set_context(intent="context_followup")
        continue

    # GREET
    if intent == "greet":
        name = get_name()
        say(f"Hello {name}" if name else "Hello")
        set_context(intent="greet")

    # SET NAME
    elif intent == "set_name":
        name = intent_data["name"]
        set_name(name)
        say(f"Nice to meet you, {name}.")
        set_context(intent="set_name", entity=name)

    # GET NAME
    elif intent == "get_name":
        name = get_name()
        if name:
            say(f"Your name is {name}.")
            set_context(intent="get_name", entity=name)
        else:
            say("I don't know your name yet.")

    # EXPLAIN MEMORY
    elif intent == "explain_name":
        say("You told me your name earlier, so I remembered it.")
        set_context(intent="explain_name")

    # FILE ACTIONS
    elif intent == "write_file":
        ok, msg = write_file(
            intent_data.get("path", ""),
            intent_data.get("content", "")
        )
        say(msg)

    elif intent == "read_file":
        ok, result = read_file(intent_data.get("path", ""))
        say(result if ok else "File not found.")

    elif intent == "delete_file":
        ok, msg = delete_file(intent_data.get("path", ""))
        say(msg)

# FAREWELL
    elif intent == "farewell":
        say("See you later 👋")

    # UNKNOWN
    else:
        say("I didn’t fully understand that. Can you rephrase?")
