# core/security.py
# Phase-4 permission gate

def ask_permission(action: str) -> bool:
    print(f"Omni (security): Permission required to {action}.")
    ans = input("Allow? (yes/no): ").strip().lower()
    return ans in ["yes", "y"]
