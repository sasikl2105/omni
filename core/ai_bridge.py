def execute_ai_response(ai_name, response):
    """
    Normalize AI responses so Jarvis never crashes.
    Supports:
    - string responses
    - dict-based action responses
    """

    # ===============================
    # SIMPLE STRING RESPONSE
    # ===============================
    if isinstance(response, str):
        return f"[{ai_name.upper()}]: {response}"

    # ===============================
    # STRUCTURED RESPONSE (FUTURE)
    # ===============================
    if isinstance(response, dict):
        action = response.get("action")

        if action == "say":
            return f"[{ai_name.upper()}]: {response.get('text', '')}"

        if action == "error":
            return f"[{ai_name.upper()} ERROR]: {response.get('message', '')}"

        return f"[{ai_name.upper()}]: Unsupported action."

    # ===============================
    # FALLBACK
    # ===============================
    return f"[{ai_name.upper()}]: Invalid response format."
