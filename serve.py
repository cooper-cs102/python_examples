from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write(
                bytes(f'<marquee>test{self.path}</marquee>', 'utf8'))

print('test')
HTTPServer(('', 8000), Handler).serve_forever()
