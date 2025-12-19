from core.brain import parse as local_parse
from core.memory import get_pref

def route(text: str):
    """
    Decide whether to use local brain or advanced brain.
    """
    use_advanced = get_pref("use_advanced_brain", False)

    # Simple heuristic
    if use_advanced and len(text.split()) > 6:
        return {"engine": "advanced", "text": text}

    return {"engine": "local", "text": text, "parsed": local_parse(text)}
