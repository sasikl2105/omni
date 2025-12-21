from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from core.security import (
    issue_challenge,
    verify_challenge,
    is_session_valid
)
from core.brain import parse
from core.executor import execute


class RemoteHandler(BaseHTTPRequestHandler):

    def _json(self, code, payload):
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode() if length else "{}"

        try:
            data = json.loads(body)
        except Exception:
            return self._json(400, {"error": "Invalid JSON"})

        # ---- AUTH CHALLENGE ----
        if self.path == "/auth/challenge":
            challenge = issue_challenge()
            return self._json(200, {"challenge": challenge})

        # ---- AUTH VERIFY ----
        if self.path == "/auth/verify":
            session = verify_challenge(
                data.get("challenge"),
                data.get("response")
            )
            if not session:
                return self._json(403, {"error": "Auth failed"})
            return self._json(200, {"session": session})

        # ---- COMMAND EXECUTION ----
        if self.path == "/command":
            session = self.headers.get("X-Session")
            if not session or not is_session_valid(session):
                return self._json(403, {"error": "Invalid session"})

            text = data.get("command")
            if not text:
                return self._json(400, {"error": "No command"})

            parsed = parse(text)
            result = execute(parsed)
            return self._json(200, {"result": result})

        return self._json(404, {"error": "Unknown endpoint"})


def start_remote(port=8080):
    server = HTTPServer(("0.0.0.0", port), RemoteHandler)
    return server
