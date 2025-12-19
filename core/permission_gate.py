from core.permissions import classify_action, SAFE, SENSITIVE, CRITICAL

def request_permission(action_name: str) -> bool:
    """
    Permission gate for Omni.
    v0.9.1: text-based approval.
    """

    level = classify_action(action_name)

    if level == SAFE:
        return True

    if level == SENSITIVE:
        answer = input(
            f"[PERMISSION] Action '{action_name}' is SENSITIVE. Allow? (y/n): "
        ).strip().lower()
        return answer == "y"

    if level == CRITICAL:
        print(
            f"[PERMISSION] Action '{action_name}' is CRITICAL and BLOCKED in v0.9.1."
        )
        return False

    return False
