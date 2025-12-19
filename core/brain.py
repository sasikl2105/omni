def parse(text: str):
    t = text.lower().strip()

    # greetings
    if t in ["hi", "hello", "hey", "hai"]:
        return {"intent": "greet"}

    # explain memory / awareness
    if "how did you know my name" in t or "how do you know my name" in t:
        return {"intent": "explain_name"}

    # set name
    if t.startswith("my name is"):
        parts = t.split()
        if len(parts) >= 4:
            return {"intent": "set_name", "name": parts[-1].capitalize()}

    # get name
    if "what is my name" in t:
        return {"intent": "get_name"}

    # ethical hacking
    if t.startswith("scan port"):
        return {"intent": "studentbae"}

    # glitchwood
    if "create player" in t:
        return {"intent": "glitchwood"}

    # system info
    if "battery" in t:
        return {"intent": "battery"}

    # root commands (future)
    if t.startswith("root"):
        return {"intent": "root", "cmd": t}

    # exit
    if t in ["bye", "exit", "quit"]:
        return {"intent": "exit"}

    return {"intent": "unknown"}
