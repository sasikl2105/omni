from core.ai_memory import save_event, recall
from core.ai_bus import send, receive


def think(profile, text):
    name = profile["name"]
    abilities = profile.get("abilities", [])
    permissions = profile.get("permissions", [])

    text_l = text.lower()

    # ===== RECEIVE MESSAGES =====
    inbox = receive(name)
    if inbox:
        msgs = []
        for m in inbox:
            msgs.append(f"[{m['from']}] {m['message']}")
            save_event(name, f"Received message from {m['from']}")
        return "\n".join(msgs)

    # ===== MEMORY =====
    if text_l in ["memory", "what do you remember", "recall"]:
        past = recall(name)
        if not past:
            return "I remember nothing yet."
        return "\n".join(f"- {p['event']}" for p in past)

    # ===== SEND MESSAGE =====
    if text_l.startswith("tell "):
        try:
            _, target, msg = text.split(" ", 2)
            send(name, target, msg)
            save_event(name, f"Messaged {target}: {msg}")
            return f"Message sent to {target}."
        except Exception:
            return "Format: tell <ai_name> <message>"

    # ===== SAFETY =====
    if "delete" in text_l or "rm" in text_l:
        save_event(name, "Blocked destructive command")
        return "Command not permitted."

    # ===== ABILITIES =====
    if "monitoring" in abilities and "scan" in text_l:
        save_event(name, "Performed monitoring scan")
        return "Monitoring complete. No threats detected."

    if "defense" in abilities and "attack" in text_l:
        save_event(name, "Defense mode engaged")
        return "Defense systems armed."

    # ===== FALLBACK =====
    save_event(name, f"Received input: {text}")
    return f"I am {name}. My abilities: {', '.join(abilities)}."
