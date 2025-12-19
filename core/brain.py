import re

def parse_command(command: str) -> dict:
    command = command.lower().strip()

    # EXIT / BYE
    if re.search(r"\b(bye|goodbye|exit|quit|see you)\b", command):
        return {"intent": "exit"}

    # GREETING
    if re.search(r"\b(hi|hello|hey)\b", command):
        return {"intent": "greet"}

    # SET NAME
    match = re.search(r"my name is (.+)", command)
    if match:
        return {
            "intent": "set_name",
            "name": match.group(1).title()
        }

    # GET NAME
    if re.search(r"(what is my name|who am i)", command):
        return {"intent": "get_name"}

    # WRITE FILE
    if re.search(r"(create|write|make).*(file)", command):
        return {
            "intent": "write_file",
            "path": "sandbox/brain_output.txt",
            "content": "Created by Omni Brain v0.10.2"
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
