import threading
import os

from core.remote import start_remote
from core.ai_manager import route_to_ai

remote_server = None
remote_thread = None

print("----------------------------------------")
print("🧠 Jarvis online (AI COMMAND GATE MODE)")
print("Talk to Jarvis. Type 'exit' to quit.")
print("----------------------------------------")

while True:
    try:
        text = input("You: ").strip()
    except KeyboardInterrupt:
        print("\nJarvis: Shutdown.")
        break

    if not text:
        continue

    if text == "exit":
        print("Jarvis: Goodbye.")
        break

    # -------- REMOTE CONTROL --------
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

        print("📡 Remote server running on port 8080.")
        continue

    if text == "stop remote":
        if remote_server:
            remote_server.shutdown()
            remote_server = None
            print("Jarvis: Remote stopped.")
        else:
            print("Jarvis: Remote not running.")
        continue

    # -------- AI ROUTING --------
    response = route_to_ai(text)
    print("Jarvis:", response)
