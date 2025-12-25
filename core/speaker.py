import subprocess
from core.context import is_voice_on

def speak(text: str):
    """
    Speak text using Android TTS via Termux API.
    """
    if not is_voice_on():
        return

    try:
        subprocess.run(
            ["termux-tts-speak", text],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except Exception:
        pass
