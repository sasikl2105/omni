import sys
import os
import json

# =========================
# FIX IMPORT PATH
# =========================
ROOT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../")
)
sys.path.insert(0, ROOT_DIR)

from core.ai_brain import think

# =========================
# LOAD CONFIG
# =========================
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")

with open(CONFIG_PATH, "r") as f:
    profile = json.load(f)

print(f"{profile['name'].capitalize()} online.")

# =========================
# MAIN LOOP
# =========================
while True:
    try:
        text = input("> ").strip()
    except KeyboardInterrupt:
        print("\nOffline.")
        break

    if not text:
        continue

    if text == "exit":
        break

    response = think(profile, text)
    print(response)
