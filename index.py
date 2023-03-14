from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        response = 200
        self.send_response(response)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(bytes("Hello World !", "utf8"))
        return 