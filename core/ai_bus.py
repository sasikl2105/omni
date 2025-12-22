import json
import os
import time

BUS_DIR = os.path.expanduser("~/omni/data/bus")
os.makedirs(BUS_DIR, exist_ok=True)


def _box(name):
    return os.path.join(BUS_DIR, f"{name}.json")


def send(sender, target, message):
    box = _box(target)

    data = []
    if os.path.exists(box):
        with open(box, "r") as f:
            data = json.load(f)

    data.append({
        "from": sender,
        "time": time.time(),
        "message": message
    })

    with open(box, "w") as f:
        json.dump(data, f, indent=2)


def receive(name):
    box = _box(name)
    if not os.path.exists(box):
        return []

    with open(box, "r") as f:
        data = json.load(f)

    os.remove(box)
    return data
