import threading
from core.brain import parse
from core.executor import execute
from core.remote import start_remote


def main():
    remote_thread = None

    print("🧠 Omni online (Executor Mode)")
    print("Type commands or 'start remote', 'exit'")
    print("----------------------------------------")

    while True:
        try:
            text = input("You: ").strip()
        except KeyboardInterrupt:
            break

        if text == "exit":
            print("Omni: Goodbye.")
            break

        if text == "start remote":
            if remote_thread is None:
                remote_thread = threading.Thread(
                    target=start_remote,
                    daemon=True
                )
                remote_thread.start()
                print("Omni: Remote control started on port 8080")
            else:
                print("Omni: Remote already running")
            continue

        action = parse(text)
        result = execute(action)
        print("Omni:", result)


if __name__ == "__main__":
    main()
