from core.brain import parse
from core.memory import get_name, set_name
from personas.gamkersgpt import explain

mode = "normal"

print("Omni online (GamkersGPT-Brain). Type 'exit' to quit.")

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

    if intent == "mode":
        mode = data["mode"]
        print(f"Omni: {mode.capitalize()} mode activated.")
        continue

    if intent == "explain_hacking":
        print("Omni (GamkersGPT):")
        print(explain(text))
        continue

    print("Omni: I am still learning.")
