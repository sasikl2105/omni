import time
import random

from core.knowledge_fetcher import fetch_knowledge
from core.knowledge_memory import remember_fact, recall_fact

# Safe starter topics (can expand later)
IDLE_TOPICS = [
    "gravity",
    "photosynthesis",
    "black hole",
    "marine biology",
    "solar system",
    "artificial intelligence",
    "computer virus",
    "internet",
    "human brain",
    "climate change"
]

IDLE_INTERVAL = 60  # seconds (1 minute)


def idle_learning_loop():
    while True:
        try:
            topic = random.choice(IDLE_TOPICS)

            # Skip if already known
            if recall_fact(topic):
                time.sleep(IDLE_INTERVAL)
                continue

            content = fetch_knowledge(topic)
            if content:
                remember_fact(topic, content, source="idle-learning")

            time.sleep(IDLE_INTERVAL)

        except Exception:
            # Never crash Jarvis for background learning
            time.sleep(IDLE_INTERVAL)
