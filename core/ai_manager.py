from core.ai_registry import get_ai

def route_to_ai(text: str):
    text_l = text.lower()

    # ---------- SYSTEM / MONITOR ----------
    if any(k in text_l for k in ["cpu", "memory", "ram", "monitor"]):
        ai = get_ai("sentinel")
        if ai.locked:
            return "AI 'sentinel' is locked."
        return ai.respond(text)

    # ---------- DEFAULT: NOVA ----------
    ai = get_ai("nova")
    if ai.locked:
        return "AI 'nova' is locked."
    return ai.respond(text)
