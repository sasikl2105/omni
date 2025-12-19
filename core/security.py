# core/security.py

SESSION_AUTHORIZED = False
PIN_CODE = "1234"

def require_permission():
    global SESSION_AUTHORIZED

    if SESSION_AUTHORIZED:
        return True

    entered = input("🔐 Enter PIN to confirm: ").strip()
    if entered == PIN_CODE:
        SESSION_AUTHORIZED = True
        print("Omni: Permission granted.")
        return True
    else:
        print("Omni: Permission denied.")
        return False
