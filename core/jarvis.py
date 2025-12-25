# core/jarvis.py
# OMNI CORE — STABLE, NON-HARDCODED BRAIN

from core.intent_engine import detect_intent
from core.knowledge_fetcher import fetch_knowledge
from core.knowledge_memory import recall_fact, remember_fact
from core.role_classifier import is_role_question, extract_role
from core.speaker import speak
import re


class Omni:
    def __init__(self):
        self.voice_enabled = False

    def _say(self, text: str):
        if self.voice_enabled:
            try:
                speak(text)
            except:
                pass

    def respond(self, text: str) -> str:
        raw = text.strip()
        clean = raw.lower()

        # -------------------------
        # EXIT
        # -------------------------
        if clean == "exit":
            return "Goodbye."

        # -------------------------
        # VOICE CONTROL
        # -------------------------
        if clean == "voice on":
            self.voice_enabled = True
            return "Voice enabled."

        if clean == "voice off":
            self.voice_enabled = False
            return "Voice disabled."

        # -------------------------
        # MATH (SAFE)
        # -------------------------
        if re.fullmatch(r"[0-9\.\+\-\*\/\(\) ]+", clean):
            try:
                result = eval(clean, {"__builtins__": {}})
                return str(result)
            except:
                return "Invalid math expression."

        # -------------------------
        # ROLE QUESTIONS (LIVE SEARCH)
        # -------------------------
        if is_role_question(clean):
            role = extract_role(clean)
            if not role:
                return "Please specify the role clearly."

            # 1️⃣ Memory first
            mem = recall_fact(role)
            if mem and mem.get("content"):
                return mem["content"]

            # 2️⃣ Wikipedia live fetch
            answer = fetch_knowledge(role)
            if answer:
                remember_fact(role, answer, source="wikipedia")
                return answer

            return f"I don’t know who holds the role '{role}'."

        # -------------------------
        # INTENT
        # -------------------------
        intent = detect_intent(clean)

        if intent["intent"] == "definition":
            topic = clean.replace("what is", "").replace("who is", "").strip()

            # Memory first
            mem = recall_fact(topic)
            if mem and mem.get("content"):
                return mem["content"]

            # Live fetch
            answer = fetch_knowledge(topic)
            if answer:
                remember_fact(topic, answer, source="wikipedia")
                return answer

            return f"I don’t know who or what '{topic}' is."

        # -------------------------
        # FALLBACK
        # -------------------------
        return "I’m processing that. Try asking differently."
