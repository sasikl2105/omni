def classify(text: str) -> str:
    text = text.lower()

    if text.startswith("who is"):
        return "person"

    if text.startswith("what is") or text.startswith("define"):
        return "definition"

    return "general"
