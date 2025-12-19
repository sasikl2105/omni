import re

def parse_command(command: str) -> dict:
    """
    Convert human language into structured intent.
    v0.10.1: added conversation intents.
    """

    command = command.lower().strip()

    # EXIT / BYE
    if re.search(r"\b(bye|goodbye|exit|quit|see you)\b", command):
        return {
            "intent": "exit"
        }

    # WRITE FILE
    if re.search(r"(create|write|make).*(file)", command):
        return {
            "intent": "write_file",
            "path": "sandbox/brain_output.txt",
            "content": "Created by Omni Brain v0.10.1"
        }

    # READ FILE
    if re.search(r"(read|open).*(file)", command):
        return {
            "intent": "read_file",
            "path": "sandbox/brain_output.txt"
        }

    # DELETE FILE
    if re.search(r"(delete|remove).*(file)", command):
        return {
            "intent": "delete_file",
            "path": "sandbox/brain_output.txt"
        }

    return {
        "intent": "unknown",
        "raw": command
    }
