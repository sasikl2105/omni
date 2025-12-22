import importlib.util
import os

AIS_PATH = os.path.expanduser("~/omni/ais")
_loaded = {}

def load_ai(name):
    if name in _loaded:
        return _loaded[name]

    path = os.path.join(AIS_PATH, name, "main.py")
    if not os.path.exists(path):
        return None

    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    _loaded[name] = module.ai
    return module.ai
