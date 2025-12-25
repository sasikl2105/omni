# core/knowledge_fetcher.py
# Central knowledge fetcher for OMNI (FIXED FOR TERMUX)

from core.knowledge_memory import recall_fact, remember_fact
from core.dictionary_fetcher import lookup_word
import requests


HEADERS = {
    "User-Agent": "OMNI-AI/1.0 (https://example.com)"
}


def fetch_knowledge(topic: str) -> str | None:
    topic = topic.lower().strip()

    # 1️⃣ Memory first
    stored = recall_fact(topic)
    if stored and stored.get("content"):
        return stored["content"]

    # 2️⃣ Wikipedia (PRIMARY)
    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic.replace(' ', '_')}"
        r = requests.get(url, headers=HEADERS, timeout=5)

        if r.status_code == 200:
            data = r.json()
            if "extract" in data and data["extract"]:
                remember_fact(topic, data["extract"], source="wikipedia")
                return data["extract"]
    except Exception:
        pass

    # 3️⃣ Dictionary (LAST RESORT)
    meaning = lookup_word(topic)
    if meaning:
        remember_fact(topic, meaning, source="dictionary")
        return meaning

    return None
