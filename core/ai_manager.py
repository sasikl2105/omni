from core.title_resolver import resolve_title
from core.ai_registry import load_ai
from core.query_classifier import classify
from core.name_normalizer import normalize_name
from core.dictionary_fetcher import fetch_definition
from core.knowledge_fetcher import fetch_knowledge
from core.knowledge_memory import recall_fact, remember_fact
from core.spell_corrector import correct_word
from core.role_knowledge import get_role_holder


def route(text: str):
    text = text.strip()
    clean = text.lower()
    qtype = classify(text)

    # ================= ROLE QUESTIONS =================
    if qtype == "role":
        role = clean.replace("who is", "").strip()

        holder = get_role_holder(role)
        if holder:
            mem = recall_fact(holder)
            if mem:
                return mem["content"]

            wiki = fetch_knowledge(holder)
            if wiki:
                remember_fact(holder, wiki, source="wikipedia")
                return wiki

        return "I couldn't find reliable information about this role."

    # ================= PERSON QUESTIONS =================
    if qtype == "person":
        name = clean.replace("who is", "").strip()

        # 🔥 TITLE / NICKNAME RESOLUTION
        title_match = resolve_title(name)
        if title_match:
            name = title_match
        else:
            name = normalize_name(name)

        mem = recall_fact(name)
        if mem:
            return mem["content"]

        wiki = fetch_knowledge(name)
        if wiki:
            remember_fact(name, wiki, source="wikipedia")
            return wiki

        return "I couldn't find reliable information about this person."

    # ================= DEFINITIONS / CONCEPTS =================
    topic = (
        clean.replace("what is", "")
        .replace("define", "")
        .strip()
    )

    topic = correct_word(topic)

    mem = recall_fact(topic)
    if mem:
        return mem["content"]

    definition = fetch_definition(topic)
    if definition:
        remember_fact(topic, definition, source="dictionary")
        return definition

    wiki = fetch_knowledge(topic)
    if wiki:
        remember_fact(topic, wiki, source="wikipedia")
        return wiki

    # ================= SYSTEM / MONITORING =================
    if any(k in clean for k in ["cpu", "memory", "monitor"]):
        ai = load_ai("sentinel")
    else:
        ai = load_ai("nova")

    if not ai:
        return "No AI available."

    return ai.respond(text)
