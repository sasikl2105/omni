import json
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")


def load_config():
    if not os.path.exists(CONFIG_PATH):
        return None
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)


config = load_config()

print("Nova online.")

if not config:
    print("❌ Missing config. Shutting down.")
    exit(1)

if config.get("locked", True):
    print("🔒 Nova is locked. Awaiting activation from Jarvis.")
    exit(0)

abilities = config.get("abilities", [])
permissions = config.get("permissions", [])

while True:
    try:
        text = input("> ").strip()
    except KeyboardInterrupt:
        print("\nBye.")
        break

    if not text:
        continue

    if text.lower() in ["exit", "quit"]:
        print("Nova shutting down.")
        break

    # ---------------- BASIC CONVERSATION ----------------
    if "conversation" in abilities:
        if text.lower() in ["hello", "hi"]:
            print("Hello. I am Nova.")
            continue

        if text.lower() in ["what are you", "who are you"]:
            print(
                f"I am Nova. Abilities: {', '.join(abilities)}. "
                f"Permissions: {', '.join(permissions)}."
            )
            continue

    # ---------------- THINKING ----------------
    if "thinking" in abilities:
        print(f"I am thinking about: '{text}'")
        continue

    # ---------------- DEFAULT ----------------
    print("I understand the input, but I am not allowed to respond.")
