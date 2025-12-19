def parse(text):
    t = text.lower()

    if t.startswith("my name is"):
        return {"intent": "set_name", "name": t.split()[-1].capitalize()}

    if "what is my name" in t:
        return {"intent": "get_name"}

    if "scan port" in t:
        return {"intent": "studentbae"}

    if "create player" in t:
        return {"intent": "glitchwood"}

    if "enable wifi" in t:
        return {"intent": "root", "cmd": "wifi_on"}

    if "disable wifi" in t:
        return {"intent": "root", "cmd": "wifi_off"}

    if t in ["bye", "exit"]:
        return {"intent": "exit"}

    return {"intent": "unknown"}
