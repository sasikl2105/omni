from core.jarvis import Omni

omni = Omni()

print("----------------------------------------")
print("🧠 OMNI ONLINE — IRON MAN CORE MODE")
print("Type commands or 'exit'")
print("----------------------------------------")

while True:
    try:
        text = input("You: ").strip()
    except KeyboardInterrupt:
        break

    if not text:
        continue

    reply = omni.respond(text)
    print("OMNI:", reply)

    if reply.lower() == "goodbye.":
        break
