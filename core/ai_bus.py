import queue

# =========================
# GLOBAL EVENT BUS
# =========================
_event_queue = queue.Queue()

# =========================
# PRODUCER
# =========================
def emit(event: str, payload: dict):
    """
    Emit an event into the AI bus.
    """
    _event_queue.put((event, payload))

# =========================
# CONSUMER (GENERATOR)
# =========================
def consume():
    """
    Generator that yields events forever.
    """
    while True:
        event = _event_queue.get()
        yield event
