from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        response = 200
        self.send_response(response)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(bytes("Hello World !", "utf8"))
        return 
    


if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8000), handler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()