from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import json

HOST = "127.0.0.1"
PORT = 8000
ROOT = Path(__file__).resolve().parent

class AppHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_POST(self):
        if self.path != "/api/message":
            self.send_error(404, "Endpoint not found")
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            message = str(payload.get("message", "")).strip()
            if not message:
                self.send_json(400, {"ok": False, "error": "Please enter a message."})
                return
            response = {
                "ok": True,
                "received": message,
                "reply": f"Server received your message: {message}",
                "server": "Local Client-Server Demo",
                "status": "Communication successful"
            }
            self.send_json(200, response)
            print(f"[CLIENT -> SERVER] {message}")
            print("[SERVER -> CLIENT] Response sent successfully")
        except (json.JSONDecodeError, UnicodeDecodeError):
            self.send_json(400, {"ok": False, "error": "Invalid JSON request."})

    def send_json(self, status, data):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

if __name__ == "__main__":
    print(f"Server running at http://{HOST}:{PORT}")
    print("Open the URL in your browser. Press Ctrl+C to stop.")
    ThreadingHTTPServer((HOST, PORT), AppHandler).serve_forever()
