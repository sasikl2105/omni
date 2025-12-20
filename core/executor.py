# core/executor.py
# Phase-4 safe command execution

import subprocess

ALLOWED_COMMANDS = {
    "nmap": ["-sn"]
}

def run_nmap_scan(target: str):
    try:
        cmd = ["nmap", "-sn", target]
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.stdout if result.stdout else result.stderr
    except Exception as e:
        return f"Execution error: {e}"
