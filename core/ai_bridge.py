import subprocess
import os

AIS_DIR = os.path.expanduser("~/omni/ais")

def run_ai(ai_name):
    ai_path = os.path.join(AIS_DIR, ai_name)
    main_file = os.path.join(ai_path, "main.py")

    if not os.path.exists(main_file):
        return None

    return subprocess.Popen(
        ["python", main_file],
        cwd=ai_path,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
