import os

# Absolute path to Omni sandbox directory
BASE_SANDBOX = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "sandbox")
)

def ensure_sandbox():
    """
    Make sure sandbox exists.
    Omni must never work outside this.
    """
    os.makedirs(BASE_SANDBOX, exist_ok=True)

def is_inside_sandbox(path: str) -> bool:
    """
    Check whether a path is inside sandbox.
    Prevents system damage.
    """
    abs_path = os.path.abspath(path)
    return abs_path.startswith(BASE_SANDBOX)
