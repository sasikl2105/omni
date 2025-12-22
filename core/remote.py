from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from core.executor import execute
from core.security import issue_challenge, verify_challenge, validate_session

PORT = 8080


class RemoteHandler(BaseHTTPRequestHandler):

    def _json(self, code, payload):
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode()

        try:
            data = json.loads(body) if body else {}
        except Exception:
            return self._json(400, {"error": "Invalid JSON"})

        # -------- AUTH --------
        if self.path == "/auth/challenge":
            return self._json(200, {"challenge": issue_challenge()})

        if self.path == "/auth/verify":
            session = verify_challenge(
                data.get("challenge"),
                data.get("response")
            )
            if not session:
                return self._json(403, {"error": "Auth failed"})
            return self._json(200, {"session": session})

        # -------- COMMAND --------
        if self.path == "/command":
            session = self.headers.get("X-Session")
            if not session or not validate_session(session):
                return self._json(403, {"error": "Invalid session"})

            cmd = data.get("command")
            if not cmd:
                return self._json(400, {"error": "No command"})

            result = execute({"command": cmd}, source="remote")
            return self._json(200, {"result": result})

        return self._json(404, {"error": "Not found"})


def start_remote():
    return HTTPServer(("127.0.0.1", PORT), RemoteHandler)
