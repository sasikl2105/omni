# core/context.py

_CONTEXT = {
    "last_intent": None,
    "last_entity": None
}

def set_context(intent=None, entity=None):
    if intent:
        _CONTEXT["last_intent"] = intent
    if entity:
        _CONTEXT["last_entity"] = entity

def get_context():
    return _CONTEXT.copy()

def clear_context():
    _CONTEXT["last_intent"] = None
    _CONTEXT["last_entity"] = None
