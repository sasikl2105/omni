import threading
from core.idle_learner import idle_learning_loop
from core.ai_manager import route
from core.executor import execute

print("----------------------------------------")
print("🧠 Jarvis online (STABLE CORE MODE)")
print("Type commands or 'exit'")
print("----------------------------------------")

ACTION_PREFIXES = (
    "deploy ",
    "run ",
    "system info",
    "list files",
    "pwd",
    "create ai"
)

while True:
    try:
        text = input("You: ").strip()
    except KeyboardInterrupt:
        break

    if not text:
        continue

    if text == "exit":
        print("Jarvis: Goodbye.")
        break

    # ===============================
    # 🔥 ACTION INTERCEPT (VENOM)
    # ===============================
    if text.startswith(ACTION_PREFIXES):
        result = execute({"command": text})
        print("Jarvis:", result)
        continue

    # ===============================
    # 🧠 AI ROUTING
    # ===============================
    response = route(text)
    if response:
        print("Jarvis:", response)

    # Start background idle learning
    idle_thread = threading.Thread(
        target=idle_learning_loop,
        daemon=True
    )
    idle_thread.start()
