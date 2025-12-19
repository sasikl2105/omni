import subprocess

def speak(text: str):
    """
    Speak text using Android TTS via Termux API.
    Fails silently if TTS is unavailable.
    """
    try:
        subprocess.run(
            ["termux-tts-speak", text],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except Exception:
        pass
