# core/ai_bridge.py
from core.ai_registry import get_ai

def explain_event(event):
    nova = get_ai("nova")
    if not nova:
        return "Nova not available."

    etype = event["type"]
    payload = event["payload"]

    if etype == "cpu_alert":
        return nova.respond(
            f"CPU usage is very high at {payload['usage']}%. "
            "Explain what this means."
        )

    if etype == "mem_alert":
        return nova.respond(
            f"Memory usage is very high at {payload['usage']}%. "
            "Explain what this means."
        )

    return "Unknown event."
