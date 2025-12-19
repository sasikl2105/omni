from core.memory_persistent import get, set

def get_name():
    return get("user.name")

def set_name(name):
    set("user.name", name)

def get_pref(k, d=None):
    return get(f"preferences.{k}", d)

def set_pref(k, v):
    set(f"preferences.{k}", v)
