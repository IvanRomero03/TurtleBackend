from http.server import BaseHTTPRequestHandler
#from urllib import parse
import json
from .src.Parser import Parser
import os
#from RedisDB import RedisDB

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
        parser = Parser()
        result = parser.parse(textInput)
        parser.execute()
        print(os.getcwd())
        #create empty file
        open("/temp/temp.svg", "w").close()
        parser.save("/temp/temp.svg")

        response = 200
        self.send_response(response)
        # send the svg file
        self.send_header('Content-type','image/svg+xml')
        self.end_headers()
        with open("/temp/temp.svg", "rb") as f:
            self.wfile.write(f.read())
        return

        # self.send_header('Content-type','text/html')
        # self.end_headers()
        # self.wfile.write(bytes("Hello World !", "utf8"))
        return
    

if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), handler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()

