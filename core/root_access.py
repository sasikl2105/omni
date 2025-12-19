import subprocess
from core.security import require_permission

ALLOWED_COMMANDS = {
    "reboot": ["reboot"],
    "wifi_on": ["svc", "wifi", "enable"],
    "wifi_off": ["svc", "wifi", "disable"],
}

def run_root(command_key):
    if command_key not in ALLOWED_COMMANDS:
        return "Command not allowed."

    if not require_permission():
        return "Permission denied."

    try:
        subprocess.run(
            ["su", "-c"] + ALLOWED_COMMANDS[command_key],
            check=True
        )
        return f"Executed {command_key}"
    except Exception as e:
        return f"Root command failed: {e}"
