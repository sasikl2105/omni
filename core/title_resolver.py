from core.title_memory import get_title

def resolve_title(text: str):
    """
    Try resolving learned titles only.
    No guessing. No hardcoding.
    """
    record = get_title(text)
    if not record:
        return None

    # confidence gate
    if record.get("confidence", 0) >= 0.7:
        return record["person"]

    return None
