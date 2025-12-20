# core/brain.py
# Phase-2 brain with execution intents

def parse(text: str) -> dict:
    t = text.lower().strip()

    if t.startswith("my name is"):
        return {"intent": "set_name", "name": t.replace("my name is", "").strip().capitalize()}

    if "what is my name" in t:
        return {"intent": "get_name"}

    if t in ["hi", "hello", "hey"]:
        return {"intent": "greet"}

    if t in ["exit", "bye"]:
        return {"intent": "exit"}

    # ---- explain mode ----
    if t.startswith("explain "):
        return {"intent": "explain_tool", "tool": t.replace("explain ", "").strip()}

    # ---- execution mode ----
    if t.startswith("scan network"):
        target = t.replace("scan network", "").strip() or "127.0.0.1"
        return {"intent": "scan_network", "target": target}

    if t.startswith("scan port"):
        parts = t.split()
        if len(parts) >= 4:
            return {
                "intent": "scan_port",
                "port": parts[2],
                "target": parts[3]
            }

    return {"intent": "unknown"}
