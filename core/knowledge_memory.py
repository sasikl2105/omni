import json
import os
import time

# ===============================
# PATH
# ===============================

KNOWLEDGE_PATH = os.path.expanduser(
    "~/omni/data/memory/knowledge.json"
)

# ===============================
# FILE HELPERS
# ===============================

def _load():
    if not os.path.exists(KNOWLEDGE_PATH):
        return {}
    with open(KNOWLEDGE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def _save(data):
    os.makedirs(os.path.dirname(KNOWLEDGE_PATH), exist_ok=True)
    with open(KNOWLEDGE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

# ===============================
# MEMORY DECAY ENGINE
# ===============================

def _apply_decay(record):
    """
    Gradually reduce confidence over time
    """
    learned_at = record.get("learned_at", time.time())
    age_seconds = time.time() - learned_at

    # 1% confidence loss per day
    decay = (age_seconds / 86400) * 0.01

    record["confidence"] = max(
        0.0,
        record.get("confidence", 0.5) - decay
    )

    return record

# ===============================
# PUBLIC API
# ===============================

def remember_fact(topic, content, source="self"):
    """
    Store or reinforce a fact
    """
    data = _load()
    key = topic.lower()

    if key in data:
        # reinforce existing memory
        data[key]["confidence"] = min(
            1.0,
            data[key].get("confidence", 0.5) + 0.1
        )
        data[key]["usage_count"] = data[key].get("usage_count", 0) + 1
        data[key]["content"] = content
    else:
        # create new memory
        data[key] = {
            "content": content,
            "source": source,
            "confidence": 0.6,
            "usage_count": 1,
            "learned_at": time.time()
        }

    _save(data)

def recall_fact(topic):
    """
    Recall memory safely (backward compatible)
    """
    data = _load()
    key = topic.lower()

    record = data.get(key)
    if not record:
        return None

    # 🔁 BACKWARD COMPATIBILITY UPGRADE
    if "confidence" not in record:
        record["confidence"] = 0.5

    if "usage_count" not in record:
        record["usage_count"] = 0

    if "learned_at" not in record:
        record["learned_at"] = time.time()

    # Apply decay
    record = _apply_decay(record)

    # Strengthen on use
    record["usage_count"] += 1
    record["confidence"] = min(1.0, record["confidence"] + 0.02)

    data[key] = record
    _save(data)

    return record

def confidence_tone(confidence: float) -> str:
    if confidence >= 0.8:
        return "I’m confident about this:"
    if confidence >= 0.5:
        return "This should be correct:"
    return "I may be mistaken, but:"
