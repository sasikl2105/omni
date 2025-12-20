# core/context.py
# Short-term conversational context (RAM only)

_context = {
    "intent": None,
    "explanation": None,
    "mode": "normal"   # normal | hacker | teacher | builder
}

def set_context(intent=None, explanation=None):
    if intent:
        _context["intent"] = intent
    if explanation:
        _context["explanation"] = explanation

def get_last_explanation():
    return _context["explanation"]

def get_mode():
    return _context["mode"]

def set_mode(mode: str):
    _context["mode"] = mode
