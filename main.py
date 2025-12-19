from core.brain import parse_command
from core.executor import write_file, read_file, delete_file
from core.memory import set_name, get_name
from core.context import set_context, get_context
from core.voice import listen
from core.speaker import speak

print("Omni v0.12.4 online.")

def say(text: str):
    print("Omni:", text)
    speak(text)

# -------- INPUT MODE SETUP (ONCE) --------
input_mode = None
while input_mode not in ["text", "voice"]:
    choice = input("Choose input mode (text/voice): ").strip().lower()
    if choice in ["text", "voice"]:
        input_mode = choice
    else:
        print("Please type 'text' or 'voice'.")

say(f"{input_mode.capitalize()} mode activated.")
print("You can say or type 'switch to voice mode' or 'switch to text mode'.")
print("Say 'bye' or 'exit' to quit.")

# -------- MAIN LOOP --------
while True:
    context = get_context()

    # INPUT (TEXT-FIRST DESIGN)
    if input_mode == "voice":
        spoken = listen()
        if spoken:
            print(f"You (voice): {spoken}")
            user_input = spoken
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

    # MODE SWITCH (EXPLICIT ONLY)
    if "switch to voice" in lower_input:
        input_mode = "voice"
        say("Voice mode activated.")
        continue

    if "switch to text" in lower_input or "voice off" in lower_input:
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

    # FAREWELL (NON-EXIT)
    elif intent == "farewell":
        say("See you later 👋")

    # FILE OPS
    elif intent == "write_file":
        ok, msg = write_file(intent_data.get("path", ""), intent_data.get("content", ""))
        say(msg)

    elif intent == "read_file":
        ok, result = read_file(intent_data.get("path", ""))
        say(result if ok else "File not found.")

    elif intent == "delete_file":
        ok, msg = delete_file(intent_data.get("path", ""))
        say(msg)

    # UNKNOWN
    else:
        say("I didn’t fully understand that. Can you rephrase?")
