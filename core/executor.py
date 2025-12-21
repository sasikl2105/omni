import os
import subprocess

def execute(action: dict) -> str:
    """
    Execute SAFE local commands only
    """

    command = action.get("command")

    if command == "system_info":
        return os.popen("uname -a").read()

    if command == "list_files":
        path = action.get("path", ".")
        try:
            return "\n".join(os.listdir(path))
        except Exception as e:
            return f"Error: {e}"

    if command == "read_file":
        filename = action.get("file")
        if not filename:
            return "No file provided"

        try:
            with open(filename, "r") as f:
                return f.read()
        except Exception as e:
            return f"Error reading file: {e}"

    if command == "shell":
        shell_cmd = action.get("shell_cmd")
        if not shell_cmd:
            return "No shell command provided"

        try:
            output = subprocess.check_output(
                shell_cmd,
                shell=True,
                stderr=subprocess.STDOUT,
                timeout=5
            )
            return output.decode()
        except Exception as e:
            return f"Shell error: {e}"

    return "Action not allowed or unknown"
