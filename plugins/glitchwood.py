import os

BASE = "sandbox/Glitchwood"

def create_player():
    os.makedirs(BASE, exist_ok=True)
    path = f"{BASE}/player.py"
    with open(path, "w") as f:
        f.write(
            "class Player:\n"
            "    def __init__(self):\n"
            "        self.health = 100\n\n"
            "    def move(self):\n"
            "        pass\n"
        )
    return "Glitchwood player created."

def create_enemy():
    os.makedirs(BASE, exist_ok=True)
    path = f"{BASE}/enemy.py"
    with open(path, "w") as f:
        f.write(
            "class Enemy:\n"
            "    def __init__(self):\n"
            "        self.damage = 10\n"
        )
    return "Glitchwood enemy created."
