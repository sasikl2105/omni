# core/advanced_brain.py
# Mode-aware reasoning (Studentbae++)

from core.context import get_mode

def explain_intent(intent: str, raw: str):
    mode = get_mode()

    if intent == "set_name":
        return "You are telling me your name so I can remember you."

    if intent == "get_name":
        return "You are checking whether I remember your identity."

    if intent == "scan":
        if mode == "hacker":
            return "You want to perform an ethical network scan for security analysis."
        return "You want to scan a network. This must be done ethically."

    if intent == "mode":
        return f"Switching operational mode."

    if intent == "exit":
        return "You want to end the conversation."

    if mode == "teacher":
        return "I am analyzing your question in an educational way."

    return "I am trying to understand your request."

def ethical_check(intent: str):
    if intent == "scan":
        return True, "Only scan systems you own or have permission for."
    return True, ""
