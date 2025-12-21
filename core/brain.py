def parse(text: str) -> dict:
    text = text.lower().strip()

    if text in ["system info", "system information"]:
        return {"command": "system_info"}

    if text in ["list files", "ls"]:
        return {"command": "list_files"}

    if text.startswith("run "):
        return {
            "command": "shell",
            "shell_cmd": text.replace("run ", "", 1)
        }

    return {"command": "unknown"}
