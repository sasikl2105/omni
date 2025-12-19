import json
import os
import hashlib

SECURITY_FILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "security.json"
)

def _load():
    with open(SECURITY_FILE, "r") as f:
        return json.load(f)

def _save(data):
    with open(SECURITY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def _hash(pin: str) -> str:
    return hashlib.sha256(pin.encode()).hexdigest()

def has_pin() -> bool:
    return _load().get("pin_hash") is not None

def set_pin(pin: str):
    data = _load()
    data["pin_hash"] = _hash(pin)
    _save(data)

def verify_pin(pin: str) -> bool:
    data = _load()
    return data.get("pin_hash") == _hash(pin)
