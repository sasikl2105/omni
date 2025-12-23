from core.ai_registry import load_ai
from core.knowledge_memory import recall, remember
from core.knowledge_fetcher import search_web

def route(text: str):
    text_l = text.lower()

    # ---------- 1. CHECK KNOWLEDGE MEMORY ----------
    known = recall(text)
    if known:
        return known["answer"]

    # ---------- 2. ROUTE TO AIs ----------
    if any(k in text_l for k in ["cpu", "memory", "monitor"]):
        ai = load_ai("sentinel")
        if ai:
            return ai.respond(text)

    ai = load_ai("nova")
    if ai:
        response = ai.respond(text)
        if response and "I am restricted" not in response:
            return response

    # ---------- 3. WEB LEARNING ----------
    learned = search_web(text)
    if learned:
        remember(text, learned)
        return learned

    return "I don't know yet, but I will learn."
