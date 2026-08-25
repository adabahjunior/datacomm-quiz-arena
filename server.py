"""Simple local server for DataComm Quiz Arena."""
import http.server
import socketserver
import webbrowser
from pathlib import Path

PORT = 8080
DIR = Path(__file__).parent


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIR), **kwargs)


if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}"
        print(f"DataComm Quiz Arena running at {url}")
        print("Press Ctrl+C to stop")
        webbrowser.open(url)
        httpd.serve_forever()
