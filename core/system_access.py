import os

def is_root():
    return os.geteuid() == 0 if hasattr(os, "geteuid") else False

def battery_status():
    try:
        with open("/sys/class/power_supply/battery/capacity") as f:
            return f"Battery {f.read().strip()}%"
    except:
        return "Battery info unavailable."

def secure_mode():
    if not is_root():
        return "Root required for secure mode."
    return "Secure mode enabled (simulated)."
