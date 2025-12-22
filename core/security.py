import hashlib
import secrets
import time

# =========================
# CONFIG
# =========================
PASSWORD = "jarvis-secret"   # later move to env
SESSION_TTL = 600            # 10 minutes

# =========================
# STATE (RAM ONLY)
# =========================
_challenges = {}
_sessions = {}

# =========================
# AUTH
# =========================
def issue_challenge():
    challenge = secrets.token_hex(16)
    _challenges[challenge] = time.time()
    return challenge


def verify_challenge(challenge, response):
    if challenge not in _challenges:
        return None

    expected = hashlib.sha256(
        (PASSWORD + challenge).encode()
    ).hexdigest()

    if expected != response:
        return None

    session = secrets.token_hex(24)
    _sessions[session] = time.time() + SESSION_TTL

    del _challenges[challenge]
    return session


def validate_session(session):
    expiry = _sessions.get(session)
    if not expiry:
        return False

    if time.time() > expiry:
        del _sessions[session]
        return False

    return True
