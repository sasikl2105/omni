# core/wake_word.py
# Simple Wake Word Engine (Phone-safe)

WAKE_WORDS = ["hey omni", "ok omni", "omni"]

def detect_wake(text: str) -> bool:
    text = text.lower().strip()
    return any(text.startswith(w) for w in WAKE_WORDS)

def strip_wake(text: str) -> str:
    text = text.lower().strip()
    for w in WAKE_WORDS:
        if text.startswith(w):
            return text[len(w):].strip()
    return text
