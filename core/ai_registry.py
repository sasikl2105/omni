import json
import importlib.util
from pathlib import Path

AIS_DIR = Path(__file__).resolve().parent.parent / "ais"
_loaded = {}

class AIWrapper:
    def __init__(self, name, module, config):
        self.name = name
        self.module = module
        self.config = config

        # 🔓 Exposed properties
        self.locked = config.get("locked", True)
        self.abilities = config.get("abilities", [])
        self.permissions = config.get("permissions", [])

    def respond(self, text: str):
        if hasattr(self.module, "respond"):
            return self.module.respond(text, self.config)
        return "AI module has no respond() method."


def _load_ai(ai_name: str):
    ai_path = AIS_DIR / ai_name
    if not ai_path.exists():
        return None

    config_path = ai_path / "config.json"
    main_path = ai_path / "main.py"

    if not config_path.exists() or not main_path.exists():
        return None

    with open(config_path, "r") as f:
        config = json.load(f)

    spec = importlib.util.spec_from_file_location(
        f"ais.{ai_name}", main_path
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return AIWrapper(ai_name, module, config)


def get_ai(ai_name: str):
    if ai_name not in _loaded:
        ai = _load_ai(ai_name)
        if not ai:
            return None
        _loaded[ai_name] = ai

    return _loaded[ai_name]
