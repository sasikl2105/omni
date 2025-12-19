import re

COMMON_FIXES = {
    "helo": "hello",
    "hii": "hi",
    "mt": "my",
    "y": "my",
    "nmae": "name",
    "latee": "later"
}

def normalize(text: str) -> str:
    text = text.lower().strip()
    for wrong, correct in COMMON_FIXES.items():
        text = re.sub(rf"\b{wrong}\b", correct, text)
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text


def fuzzy_contains(text: str, keywords: list) -> int:
    score = 0
    for word in keywords:
        if word in text:
            score += 1
    return score


def parse_command(raw_command: str) -> dict:
    command = normalize(raw_command)

    # EXIT
    if fuzzy_contains(command, ["exit", "quit", "bye"]) >= 1:
        return {"intent": "exit"}

    # FAREWELL (NON-EXIT)
    if fuzzy_contains(command, ["see", "later"]) >= 2 or \
       fuzzy_contains(command, ["talk", "later"]) >= 2 or \
       fuzzy_contains(command, ["see", "ya"]) >= 1:
        return {"intent": "farewell"}

    # GREET
    if fuzzy_contains(command, ["hi", "hello", "hey"]) >= 1:
        return {"intent": "greet"}

    # QUESTION INTENTS
    if command.startswith("what") or command.startswith("who") or command.startswith("how"):
        if "name" in command:
            return {"intent": "get_name"}
        if fuzzy_contains(command, ["how", "know", "name"]) >= 2:
            return {"intent": "explain_name"}

    # SET NAME
    if fuzzy_contains(command, ["my", "name", "is"]) >= 2:
        match = re.search(r"(?:my\s+name\s+is\s+)(\w+)", command)
        if match:
            return {
                "intent": "set_name",
                "name": match.group(1).capitalize()
            }
        return {"intent": "ask_name"}

    return {"intent": "unknown"}
