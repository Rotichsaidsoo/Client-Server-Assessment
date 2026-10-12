from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import json
import os

HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", 8000))
ROOT = Path(file).resolve().parent

class AppHandler(SimpleHTTPRequestHandler):
def init(self, *args, **kwargs):
super().init(*args, directory=str(ROOT), **kwargs)

def do_POST(self):
    if self.path != "/api/message":
        self.send_error(404, "Endpoint not found")
        return

    try:
        length = int(self.headers.get("Content-Length", "0"))
        payload = json.loads(
            self.rfile.read(length).decode("utf-8")
        )

        message = str(payload.get("message", "")).strip()

        if not message:
            self.send_json(
                400,
                {"ok": False, "error": "Please enter a message."}
            )
            return

        response = {
            "ok": True,
            "received": message,
            "reply": f"Server received your message: {message}",
            "server": "Client-Server Demo",
            "status": "Communication successful"
        }

        self.send_json(200, response)
        print(f"[CLIENT -> SERVER] {message}")
        print("[SERVER -> CLIENT] Response sent successfully")

    except (json.JSONDecodeError, UnicodeDecodeError):
        self.send_json(
            400,
            {"ok": False, "error": "Invalid JSON request."}
        )

def send_json(self, status, data):
    body = json.dumps(data).encode("utf-8")
    self.send_response(status)
    self.send_header(
        "Content-Type", "application/json; charset=utf-8"
    )
    self.send_header("Content-Length", str(len(body)))
    self.end_headers()
    self.wfile.write(body)

if name == "main":
server = ThreadingHTTPServer((HOST, PORT), AppHandler)
print(f"Server listening on {HOST}:{PORT}")
server.serve_forever()