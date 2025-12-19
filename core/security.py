PIN = "1234"
AUTHORIZED = False

def require_permission():
    global AUTHORIZED
    if AUTHORIZED:
        return True
    p = input("🔐 Enter PIN: ").strip()
    if p == PIN:
        AUTHORIZED = True
        print("Omni: Permission granted.")
        return True
    print("Omni: Permission denied.")
    return False
