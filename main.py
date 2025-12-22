import threading
import sys

from core.executor import execute
from core.remote import start_remote
from core.ai_registry import list_ais
from core.ai_bridge import run_ai

remote_server = None
remote_thread = None

active_ai = None
ai_process = None

print("🧠 Jarvis online (OMNITRIX MODE)")
print("Commands: start remote | talk to <ai> | exit ai | exit")
print("------------------------------------------------------")

while True:
    try:
        text = input("You: ").strip()
    except KeyboardInterrupt:
        print("\nJarvis: Shutdown.")
        break

    if not text:
        continue

    # ================= AI MODE =================
    if active_ai:
        if text == "exit ai":
            ai_process.terminate()
            ai_process = None
            active_ai = None
            print("Jarvis: Returned to control.")
            continue

        ai_process.stdin.write(text + "\n")
        ai_process.stdin.flush()

        reply = ai_process.stdout.readline().strip()
        print(f"{active_ai}:", reply)
        continue

    # ================= EXIT =================
    if text == "exit":
        print("Jarvis: Goodbye.")
        break

    # ================= REMOTE =================
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
        print("📡 Remote server started on port 8080")
        continue

    # ================= TALK TO AI =================
    if text.startswith("talk to "):
        ai_name = text.replace("talk to ", "").strip()

        if ai_name not in list_ais():
            print(f"Jarvis: AI '{ai_name}' not found.")
            continue

        ai_process = run_ai(ai_name)
        if not ai_process:
            print("Jarvis: Failed to start AI.")
            continue

        active_ai = ai_name
        print(f"Jarvis: Connected to {ai_name}.")
        continue

    # ================= LOCAL =================
    result = execute({"command": text})
    print("Jarvis:", result)
