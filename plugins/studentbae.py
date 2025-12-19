from core.hacking_tools import port_scan

def handle(command: str):
    parts = command.lower().split()

    port = None
    host = None

    # Find port number
    for p in parts:
        if p.isdigit():
            port = int(p)
            break

    # Find host (last non-numeric token)
    for p in reversed(parts):
        if not p.isdigit() and p not in ["scan", "port"]:
            host = p
            break

    if port is None or host is None:
        return "Invalid scan command. Use: scan port <port> <host>"

    return port_scan(host, port)
