def classify(text: str) -> str:
    text = text.lower().strip()

    # PERSON QUESTIONS
    if text.startswith("who is"):
        return "person"

    # DEFINITIONS / MEANINGS
    if (
        text.startswith("what is")
        or text.startswith("define")
        or text.startswith("what does")
        or text.endswith("mean")
    ):
        return "definition"

    return "general"
