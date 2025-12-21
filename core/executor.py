import os
import subprocess

ALLOWED_COMMANDS = {
    "system info": "system_info",
    "system_info": "system_info",
    "list files": "list_files",
    "list_files": "list_files",
    "run": "shell",
}

def execute(action: dict) -> str:
    cmd = action.get("command", "").strip().lower()

    if cmd not in ALLOWED_COMMANDS:
        return "Action not allowed."

    cmd_key = ALLOWED_COMMANDS[cmd]

    # ---- SYSTEM INFO ----
    if cmd_key == "system_info":
        return os.popen("uname -a").read()

    # ---- LIST FILES ----
    if cmd_key == "list_files":
        path = action.get("path", ".")
        try:
            return "\n".join(os.listdir(path))
        except Exception as e:
            return f"Error: {e}"

    # ---- SHELL COMMAND ----
    if cmd_key == "shell":
        shell_cmd = action.get("shell_cmd")
        if not shell_cmd:
            return "No shell command provided."

        try:
            out = subprocess.check_output(
                shell_cmd,
                shell=True,
                stderr=subprocess.STDOUT,
                timeout=5
            )
            return out.decode()
        except Exception as e:
            return f"Shell error: {e}"

    return "Unhandled command."
