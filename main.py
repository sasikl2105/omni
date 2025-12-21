from core.brain import parse
from core.executor import execute

def main():
    print("🧠 Omni online (Executor Mode)")
    print("Type commands or 'exit'")
    print("-" * 40)

    while True:
        try:
            user_input = input("You: ").strip()

            if user_input.lower() in ["exit", "quit"]:
                print("👋 Omni shutting down")
                break

            action = parse(user_input)

            if action.get("command") == "unknown":
                print("Omni: I don't understand that yet.")
                continue

            result = execute(action)
            print("Omni:", result)

        except KeyboardInterrupt:
            print("\n👋 Interrupted")
            break

        except Exception as e:
            print("❌ Error:", e)

if __name__ == "__main__":
    main()
