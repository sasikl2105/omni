import os
import subprocess


def execute(action: dict) -> str:
    """
    Executes SAFE actions approved by the brain.
    """

    cmd = action.get("command")

    if cmd == "system_info":
        return os.popen("uname -a").read()

    if cmd == "list_files":
        path = action.get("path", ".")
        try:
            return "\n".join(os.listdir(path))
        except Exception as e:
            return f"Error: {e}"

    if cmd == "shell":
        shell_cmd = action.get("shell_cmd")
        if not shell_cmd:
            return "No shell command provided."

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

    return "Action not allowed."
