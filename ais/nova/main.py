from core.ai_memory import remember, recall

class NovaAI:
    name = "nova"

    def respond(self, text):
        remember("nova", "user", text)

        if "gravity" in text.lower():
            reply = "Gravity is the force that pulls objects toward each other."
        elif "cpu" in text.lower():
            reply = "CPU usage appears elevated due to running processes."
        elif "memory" in text.lower():
            reply = "Memory usage is within acceptable limits."
        else:
            reply = f"You said: {text}"

        remember("nova", "assistant", reply)
        return reply


# 🔥 THIS IS WHAT JARVIS EXPECTS
ai = NovaAI()
