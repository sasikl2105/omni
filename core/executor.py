import os
from core.sandbox import ensure_sandbox, is_inside_sandbox

ensure_sandbox()

def write_file(path: str, content: str):
    if not is_inside_sandbox(path):
        return False, "Blocked: outside sandbox"

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    return True, "File written successfully"

def read_file(path: str):
    if not is_inside_sandbox(path):
        return False, "Blocked: outside sandbox"

    if not os.path.exists(path):
        return False, "File not found"

    with open(path, "r", encoding="utf-8") as f:
        return True, f.read()

def delete_file(path: str):
    if not is_inside_sandbox(path):
        return False, "Blocked: outside sandbox"

    if not os.path.exists(path):
        return False, "File not found"

    os.remove(path)
    return True, "File deleted"
