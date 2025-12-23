import os
import subprocess
from core.deployer import deploy_to_host

SAFE_COMMANDS = [
    "system info",
    "list files",
    "pwd"
]

def execute(action: dict) -> str:
    cmd = action.get("command", "").strip()

    # ================= SYSTEM INFO =================
    if cmd == "system info":
        return os.popen("uname -a").read()

    if cmd == "list files":
        return "\n".join(os.listdir("."))

    if cmd == "pwd":
        return os.getcwd()

    # ================= DEPLOY (VENOM MODE) =================
    if cmd.startswith("deploy "):
        try:
            target = cmd.replace("deploy ", "").strip()
            user, host = target.split("@")
            return deploy_to_host(user, host)
        except Exception as e:
            return f"❌ Deploy failed: {e}"

    # ================= SHELL =================
    if cmd.startswith("run "):
        shell_cmd = cmd.replace("run ", "", 1)

        # HARD BLOCK
        if "rm -rf /" in shell_cmd:
            return "❌ Shell command blocked for safety."

        try:
            return subprocess.check_output(
                shell_cmd,
                shell=True,
                stderr=subprocess.STDOUT,
                timeout=5
            ).decode()
        except Exception as e:
            return f"❌ Command failed: {e}"

    # ================= AI CREATION =================
    if cmd.startswith("create ai"):
        try:
            parts = cmd.replace("create ai", "").strip().split(":")
            name = parts[0].strip()
            abilities = [a.strip() for a in parts[1].split(",")]
        except Exception:
            return "Usage: create ai <name> : ability1, ability2"

        from core.ai_forge import create_ai
        return create_ai(name, abilities)

    return "Action not allowed."
