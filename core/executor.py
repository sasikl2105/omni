# core/executor.py

import os

def write_file(path: str, content: str):
    try:
        with open(path, "w") as f:
            f.write(content)
        return True, f"File '{path}' written successfully."
    except Exception as e:
        return False, f"Failed to write file: {e}"

def read_file(path: str):
    try:
        if not os.path.exists(path):
            return False, "File does not exist."
        with open(path, "r") as f:
            return True, f.read()
    except Exception as e:
        return False, f"Failed to read file: {e}"

def delete_file(path: str):
    try:
        if not os.path.exists(path):
            return False, "File does not exist."
        os.remove(path)
        return True, f"File '{path}' deleted."
    except Exception as e:
        return False, f"Failed to delete file: {e}"
