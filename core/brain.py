def parse(text: str) -> dict:
    text = text.lower().strip()

    if "system info" in text:
        return {"command": "system_info"}

    if text.startswith("list files"):
        return {"command": "list_files"}

    if text.startswith("read"):
        parts = text.split()
        if len(parts) >= 2:
            return {"command": "read_file", "file": parts[1]}

    if text.startswith("run"):
        shell_cmd = text.replace("run", "", 1).strip()
        return {"command": "shell", "shell_cmd": shell_cmd}

    return {"command": "unknown"}
