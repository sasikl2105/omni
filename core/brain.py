import re
from core.memory import get_pending, set_pending, clear_pending

def parse_command(command: str) -> dict:
    command = command.lower().strip()
    pending = get_pending()

    # EXIT
    if re.search(r"\b(bye|exit|quit|goodbye)\b", command):
        clear_pending()
        return {"intent": "exit"}

    # HANDLE PENDING NAME
    if pending == "awaiting_name":
        if not command.strip():
            return {"intent": "wait"}  # ignore silence
        clear_pending()
        return {
            "intent": "set_name",
            "name": command.title()
        }

    # GREETING
    if re.search(r"\b(hi|hello|hey)\b", command):
        return {"intent": "greet"}

    # INCOMPLETE NAME
    if command == "my name is":
        set_pending("awaiting_name")
        return {"intent": "ask_name"}

    # COMPLETE NAME
    match = re.search(r"my name is (.+)", command)
    if match:
        return {
            "intent": "set_name",
            "name": match.group(1).title()
        }

    # GET NAME
    if re.search(r"(what is my name|who am i)", command):
        return {"intent": "get_name"}

# EXPLAIN MEMORY
    if re.search(r"(how do you know my name|who told you my name|did i tell you my name)", command):
        return {"intent": "explain_name"}

    # FILE ACTIONS
    if re.search(r"(create|write|make).*(file)", command):
        return {
            "intent": "write_file",
            "path": "sandbox/brain_output.txt",
            "content": "Created by Omni Brain v0.10.3.1"
        }

    if re.search(r"(read|open).*(file)", command):
        return {
            "intent": "read_file",
            "path": "sandbox/brain_output.txt"
        }

    if re.search(r"(delete|remove).*(file)", command):
        return {
            "intent": "delete_file",
            "path": "sandbox/brain_output.txt"
        }

    return {"intent": "unknown"}
