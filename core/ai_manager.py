import threading
import time
from core.system_access import get_cpu_usage, get_memory_usage

def background_sentinel():
    while True:
        cpu = get_cpu_usage()
        mem = get_memory_usage()

        if "Cpu" in cpu:
            print("\n🛡️ Sentinel (background): CPU check OK")

        time.sleep(30)  # check every 30 seconds


def start_background_monitor():
    t = threading.Thread(
        target=background_sentinel,
        daemon=True
    )
    t.start()


from core.ai_registry import load_ai

def route(text: str):
    text_l = text.lower()

    # Decide AI
    if any(k in text_l for k in ["cpu", "memory", "monitor", "system"]):
        ai = load_ai("sentinel")
    else:
        ai = load_ai("nova")

    if not ai:
        return "No AI available."

    # AI must respond
    if hasattr(ai, "respond"):
        return ai.respond(text)

    return "AI module has no respond() method."
