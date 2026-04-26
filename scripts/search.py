#!/usr/bin/env python3
"""
brain-search — Search Server
Serves the search UI at http://localhost:7777 and proxies Gemini embed calls.

Usage:
  python3 scripts/search.py              # start server + open browser
  python3 scripts/search.py --port 8888  # custom port
  python3 scripts/search.py --no-open   # don't auto-open browser
"""

import json, os, argparse, subprocess, urllib.request, urllib.error
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler

def load_env():
    env = Path.home() / ".claude" / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, _, v = line.partition('=')
                os.environ.setdefault(k.strip(), v.strip().strip('"\''))
load_env()

parser = argparse.ArgumentParser()
parser.add_argument('--port', type=int, default=7777)
parser.add_argument('--no-open', action='store_true')
parser.add_argument('--embeddings', default='search_data/embeddings.json')
args = parser.parse_args()

BASE         = Path(__file__).parent.parent
SEARCH_HTML  = BASE / 'scripts' / 'search.html'
EMBEDDINGS   = Path(args.embeddings)
GEMINI_KEY   = os.environ.get('GEMINI_API_KEY', '')

class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args): pass

    def send(self, code, ctype, body):
        b = body if isinstance(body, bytes) else body.encode()
        self.send_response(code)
        self.send_header('Content-Type', ctype)
        self.send_header('Content-Length', len(b))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(b)

    def do_OPTIONS(self):
        self.send_response(200)
        for h, v in [('Access-Control-Allow-Origin','*'),
                     ('Access-Control-Allow-Methods','GET,POST,OPTIONS'),
                     ('Access-Control-Allow-Headers','Content-Type')]:
            self.send_header(h, v)
        self.end_headers()

    def do_GET(self):
        if self.path in ('/', '/search'):
            self.send(200, 'text/html; charset=utf-8', SEARCH_HTML.read_text())
        elif self.path == '/embeddings.json':
            if not EMBEDDINGS.exists():
                self.send(404, 'application/json',
                    json.dumps({'error': 'No embeddings. Run: python3 scripts/embed.py'}))
            else:
                self.send(200, 'application/json', EMBEDDINGS.read_text())
        else:
            self.send(404, 'text/plain', 'Not found')

    def do_POST(self):
        if self.path != '/embed':
            self.send(404, 'text/plain', 'Not found'); return

        length = int(self.headers.get('Content-Length', 0))
        body = json.loads(self.rfile.read(length))
        text = (body.get('text') or '').strip()[:500]

        if not text:
            self.send(400, 'application/json', json.dumps({'error': 'text required'})); return
        if not GEMINI_KEY:
            self.send(500, 'application/json', json.dumps({'error': 'No GEMINI_API_KEY'})); return

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent?key={GEMINI_KEY}"
        payload = json.dumps({
            "model": "models/gemini-embedding-2",
            "content": {"parts": [{"text": text}]},
            "taskType": "RETRIEVAL_QUERY",
            "outputDimensionality": 256,
        }).encode()
        req = urllib.request.Request(url, data=payload,
            headers={"Content-Type": "application/json"}, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read())
                self.send(200, 'application/json',
                    json.dumps({'vector': data['embedding']['values']}))
        except Exception as e:
            self.send(502, 'application/json', json.dumps({'error': str(e)}))

print(f"\n  brain-search")
if not EMBEDDINGS.exists():
    print(f"  WARNING: No embeddings at {EMBEDDINGS}")
    print(f"  Run: python3 scripts/ingest.py <folder> --run")
    print(f"       python3 scripts/embed.py")
print(f"\n  http://localhost:{args.port}")
print(f"  Ctrl+C to stop\n")

if not args.no_open:
    import platform
    cmd = 'open' if platform.system() == 'Darwin' else 'xdg-open'
    subprocess.Popen([cmd, f'http://localhost:{args.port}'])

HTTPServer(('', args.port), Handler).serve_forever()
