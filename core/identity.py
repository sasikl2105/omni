# core/identity.py
# OMNI Identity & Confidence Engine

IDENTITY = {
    "name": "OMNI",
    "version": "5.1",
    "role": "Personal AI Assistant",
    "style": "calm",
    "creator": "Harish"
}

CONFIDENCE_LEVELS = {
    "high": 0.8,
    "medium": 0.5,
    "low": 0.2
}


def get_identity():
    return IDENTITY


def set_style(style: str):
    if style in ["calm", "assertive", "alert"]:
        IDENTITY["style"] = style


def confidence_phrase(confidence: float):
    if confidence >= CONFIDENCE_LEVELS["high"]:
        return "I am confident this is correct."
    elif confidence >= CONFIDENCE_LEVELS["medium"]:
        return "This should be correct."
    else:
        return "I may be mistaken, but here is what I know."
