from core.ai_manager import route
from core.ai_manager import start_background_monitor
from core.ai_manager import route
from core.ai_memory import remember

print("----------------------------------------")
print("🧠 Jarvis online (STABLE CORE MODE)")
print("Type commands or 'exit'")
print("----------------------------------------")

start_background_monitor()
while True:
    try:
        text = input("You: ").strip()
    except KeyboardInterrupt:
        print("\nJarvis: Goodbye.")
        break

    if not text:
        continue

    if text.lower() == "exit":
        print("Jarvis: Goodbye.")
        break

    # -------- ROUTE TO AI --------
    response = route(text)

    # -------- OUTPUT --------
    if response:
        print("Jarvis:", response)
    else:
        print("Jarvis: ...")

    # -------- MEMORY --------
    remember("jarvis", "user", text)
    remember("jarvis", "assistant", response)
