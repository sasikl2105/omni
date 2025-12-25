# core/context.py
# Runtime context (RAM only)

_context = {
    "intent": None,
    "explanation": None,
    "mode": "normal",   # normal | hacker | teacher | builder
    "voice": True       # 🔊 voice on by default
}

def set_context(intent=None, explanation=None):
    if intent is not None:
        _context["intent"] = intent
    if explanation is not None:
        _context["explanation"] = explanation

def get_last_explanation():
    return _context.get("explanation")

def get_mode():
    return _context.get("mode")

def set_mode(mode: str):
    _context["mode"] = mode

# 🔊 VOICE CONTROL
def is_voice_on():
    return _context.get("voice", False)

def set_voice(state: bool):
    _context["voice"] = state
