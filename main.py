import threading

from core.remote import start_remote

remote_server = None


def run_server(server):
    print("📡 Remote server running...")
    server.serve_forever()


print("🧠 Omni online (Executor Mode)")
print("Type 'start remote', 'stop remote', or 'exit'")
print("----------------------------------------")

while True:
    text = input("You: ").strip().lower()

    if text == "exit":
        print("Omni: Goodbye.")
        break

    if text == "start remote":
        if remote_server:
            print("Omni: Remote already running.")
        else:
            remote_server = start_remote(8080)
            t = threading.Thread(
                target=run_server,
                args=(remote_server,),
                daemon=True
            )
            t.start()
            print("Omni: Remote control started on port 8080")
        continue

    if text == "stop remote":
        if remote_server:
            remote_server.shutdown()
            remote_server = None
            print("Omni: Remote stopped.")
        else:
            print("Omni: Remote not running.")
        continue

    print("Omni: Unknown command.")
