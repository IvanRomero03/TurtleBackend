from http.server import BaseHTTPRequestHandler
from urllib import parse
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        s = self.path
        print(s)
        # Content-Type: application/json
        # {"text": "fd 100"}
        text = self.rfile.read(int(self.headers['Content-Length'])).decode("utf-8")
        textJson = json.dumps(text)
        print(text)
        text = json.loads(text)
        print(text)
        textInput = text["text"]
        print(textInput)
        print(text)
        response = 200
        self.send_response(response)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(bytes("Hello World !", "utf8"))
        return
    

if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), handler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()

