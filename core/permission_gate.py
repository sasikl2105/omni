from core.permissions import classify_action, SAFE, SENSITIVE, CRITICAL
from core.security import has_pin, set_pin, verify_pin

def request_permission(action_name: str) -> bool:
    level = classify_action(action_name)

    if level == SAFE:
        return True

    if level == CRITICAL:
        print(
            f"[PERMISSION] Action '{action_name}' is CRITICAL and BLOCKED in v0.9.2."
        )
        return False

    # SENSITIVE actions
    if not has_pin():
        print("[SECURITY] No PIN set.")
        new_pin = input("Set a new PIN: ").strip()
        set_pin(new_pin)
        print("[SECURITY] PIN set successfully.")

    attempt = input(
        f"[SECURITY] Enter PIN to allow '{action_name}': "
    ).strip()

    if verify_pin(attempt):
        return True

    print("[SECURITY] Incorrect PIN.")
    return False
