from core.brain import parse as local_parse
from core.memory import get_pref


def route(text: str) -> dict:
    """
    Decide which brain should handle the input.
    """

    # User preference (future toggle)
    use_advanced = get_pref("use_advanced_brain", False)

    # Heuristic: long or complex text → advanced brain
    if use_advanced and len(text.split()) > 6:
        return {
            "engine": "advanced",
            "text": text
        }

    # Default: local brain
    parsed = local_parse(text)

    return {
        "engine": "local",
        "text": text,
        "parsed": parsed
    }
