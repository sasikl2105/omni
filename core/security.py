import hashlib
import secrets
import time

# In-memory stores (Stage 4 – simple but solid)
_challenges = {}
_sessions = {}

PASSWORD = "jarvis-secret"
SESSION_TTL = 300  # 5 minutes


def issue_challenge():
    challenge = secrets.token_hex(16)
    _challenges[challenge] = time.time()
    return challenge


def verify_challenge(challenge: str, response: str):
    if challenge not in _challenges:
        return None

    expected = hashlib.sha256(
        (PASSWORD + challenge).encode()
    ).hexdigest()

    # Remove challenge (one-time use)
    del _challenges[challenge]

    if response != expected:
        return None

    # Create session
    session = secrets.token_hex(24)
    _sessions[session] = time.time()
    return session


def is_session_valid(session: str) -> bool:
    ts = _sessions.get(session)
    if not ts:
        return False

    if time.time() - ts > SESSION_TTL:
        del _sessions[session]
        return False

    return True
