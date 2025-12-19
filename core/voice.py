import subprocess
import time

def listen(timeout=4) -> str | None:
    """
    Try to capture voice input.
    Returns text or None if nothing heard.
    """
    try:
        result = subprocess.run(
            ["termux-speech-to-text"],
            capture_output=True,
            text=True,
            timeout=timeout
        )

        text = result.stdout.strip()
        if text:
            return text
        return None

    except Exception:
        return None
