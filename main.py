import threading
from core.executor import execute
from core.remote import start_remote

remote_server = None
remote_thread = None

print("🧠 Jarvis online (VENOM MODE)")
print("Type commands or 'exit'")
print("----------------------------------------")

while True:
    try:
        text = input("You: ").strip()
    except KeyboardInterrupt:
        print("\nBye.")
        break

    if not text:
        continue

    if text == "exit":
        print("Jarvis: Goodbye.")
        break

    # ---------- REMOTE ----------
    if text == "start remote":
        if remote_server:
            print("Jarvis: Remote already running.")
            continue

        remote_server = start_remote()
        remote_thread = threading.Thread(
            target=remote_server.serve_forever,
            daemon=True
        )
        remote_thread.start()
        print("📡 Remote server running on port 8080")
        continue

    if text == "stop remote":
        if remote_server:
            remote_server.shutdown()
            remote_server = None
            print("Jarvis: Remote stopped.")
        else:
            print("Jarvis: Remote not running.")
        continue

    # ---------- EXECUTE ----------
    result = execute({"command": text})
    print("Jarvis:", result)
