# core/intent_engine.py
# Intent detection engine for OMNI

import re


def detect_intent(text: str) -> dict:
    text = text.lower().strip()

    # Voice
    if text in ["voice on", "enable voice"]:
        return {"intent": "voice_on"}

    if text in ["voice off", "disable voice"]:
        return {"intent": "voice_off"}

    # Name memory
    if text.startswith("remember my name as"):
        name = text.replace("remember my name as", "").strip()
        return {"intent": "remember_name", "name": name}

    # Math
    if re.search(r"[0-9\+\-\*/\(\)]", text):
        return {"intent": "math"}

    # Definition
    if (
        text.startswith("what is")
        or text.startswith("who is")
        or text.startswith("what does")
    ):
        return {"intent": "definition"}

    return {"intent": "unknown"}
