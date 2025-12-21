from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from core.brain import parse
from core.executor import execute

TOKEN = "omni-local-token"


class RemoteHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        if self.path != "/command":
            self.send_response(404)
            self.end_headers()
            return

        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode()

        try:
            data = json.loads(body)
        except Exception:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid JSON")
            return

        if data.get("token") != TOKEN:
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"Invalid token")
            return

        text = data.get("command")
        if not text:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"No command")
            return

        action = parse(text)
        result = execute(action)

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        self.wfile.write(
            json.dumps({"result": result}).encode()
        )


def start_remote(port=8080):
    server = HTTPServer(("127.0.0.1", port), RemoteHandler)
    print(f"📡 Remote server listening on http://127.0.0.1:{port}")
    server.serve_forever()
