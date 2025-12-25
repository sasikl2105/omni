import json
import os

TASK_FILE = os.path.join("data", "memory", "tasks.json")

def _load():
    if not os.path.exists(TASK_FILE):
        return {"tasks": []}
    with open(TASK_FILE, "r") as f:
        return json.load(f)

def _save(data):
    with open(TASK_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_task(task):
    data = _load()
    data["tasks"].append({
        "task": task,
        "done": False
    })
    _save(data)

def list_tasks():
    return _load()["tasks"]

def complete_task(index):
    data = _load()
    try:
        data["tasks"][index]["done"] = True
        _save(data)
        return True
    except:
        return False
