import os
import subprocess
import json

def is_android():
    return "ANDROID_ROOT" in os.environ

def battery_status():
    # Android (Termux)
    if is_android():
        try:
            result = subprocess.check_output(
                ["termux-battery-status"],
                stderr=subprocess.DEVNULL
            )
            data = json.loads(result.decode())
            return f"Battery {data.get('percentage')}% ({data.get('status')})"
        except:
            return "Battery info unavailable (Termux API not accessible)."

    # Linux (PC)
    try:
        with open("/sys/class/power_supply/battery/capacity") as f:
            return f"Battery {f.read().strip()}%"
    except:
        return "Battery info unavailable."
