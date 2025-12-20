# main.py
from core.brain import parse
from core.memory import set_name, get_name
from core.advanced_brain import explain_tool
from core.security import request_permission
from core.executor import run_nmap_scan, run_nmap_port

print("Omni online (Phase-2). Type 'exit' to quit.")

while True:
    text = input("You: ").strip()
    if not text:
        continue

    data = parse(text)
    intent = data["intent"]

    if intent == "exit":
        print("Omni: Goodbye.")
        break

    if intent == "greet":
        name = get_name()
        print(f"Omni: Hello {name}" if name else "Omni: Hello 👋")
        continue

    if intent == "set_name":
        set_name(data["name"])
        print(f"Omni: Nice to meet you, {data['name']}.")
        continue

    if intent == "get_name":
        print("Omni:", get_name() or "I don't know your name yet.")
        continue

    if intent == "explain_tool":
        print("Omni:\n" + explain_tool(data["tool"]))
        continue

    if intent == "scan_network":
        if request_permission("nmap network scan"):
            print("Omni:\n" + run_nmap_scan(data["target"]))
        continue

    if intent == "scan_port":
        if request_permission(f"nmap port scan {data['port']}"):
            print("Omni:\n" + run_nmap_port(data["target"], data["port"]))
        continue

    print("Omni: I am still learning.")
