def parse(text: str) -> dict:
    t = text.lower().strip()

    if t in ["exit", "bye", "quit"]:
        return {"intent": "exit"}

    if t.startswith("my name is"):
        name = t.replace("my name is", "").strip().capitalize()
        return {"intent": "set_name", "name": name}

    if "what is my name" in t:
        return {"intent": "get_name"}

    if "hacker mode" in t:
        return {"intent": "mode", "mode": "hacker"}

    if "teacher mode" in t:
        return {"intent": "mode", "mode": "teacher"}

    if "builder mode" in t:
        return {"intent": "mode", "mode": "builder"}

    # hacking-related questions
    if any(k in t for k in ["wifi", "password", "scan", "nmap", "hydra"]):
        return {"intent": "explain_hacking"}

    return {"intent": "unknown"}
