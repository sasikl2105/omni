import json

RULES_FILE = "rules.json"


def load_rules():
    with open(RULES_FILE, "r") as f:
        return json.load(f)


def run(input_text):
    rules = load_rules()

    # Ability check
    if "answer_questions" in rules["abilities"]:
        return f"{rules['name']} says: I can answer, but I cannot act."

    return "I am restricted and cannot respond."


if __name__ == "__main__":
    print(f"{load_rules()['name']} online.")
    while True:
        text = input("> ").strip()
        if text.lower() in ("exit", "quit"):
            break
        print(run(text))
