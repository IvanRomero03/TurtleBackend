from http.server import BaseHTTPRequestHandler
import json
from .src.Parser import Parser
import os
#from .src.handler import handlerBase 
from .src.util import randomHash
from .src.RedisDB import RedisDB

# class handler(handlerBase):
#     def do_GET(self):
#         response = 200
#         self.send_response(response)
#         self.send_header('Content-type','text/html')
#         self.end_headers()
#         self.wfile.write(bytes("Hello World !", "utf8"))
#         return
#     def do_POST(self):
#         s = self.path
#         # Content-Type: application/json
#         # {"text": "fd 100"}
#         text = self.rfile.read(int(self.headers['Content-Length'])).decode("utf-8")
#         text = json.loads(text)
#         textInput = text["text"]
#         parser = Parser()
#         result = parser.parse(textInput)
#         parser.execute()
#         # pass the result to the redis db 
#         # create a random hash
#         hash = randomHash(16)
#         self.redis.set(hash, str(result))
#         svg = parser.getSVG()

#         response = 200
#         self.send_response(response)
#         # send the svg file
#         self.send_header('Content-type','image/svg+xml')
#         self.end_headers()
#         self.wfile.write(svg.encode("utf-8"))
#         return



class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        response = 200
        self.send_response(response)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(bytes("Hello World !", "utf8"))
        return
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
        # print tree 
        print(os.listdir())
        #create empty file
        #open("/temp/temp.svg", "w").close()
        svg = parser.getSVG()

        response = 200
        self.send_response(response)
        # send the svg file
        self.send_header('Content-type','image/svg+xml')
        self.end_headers()
        self.wfile.write(svg.encode("utf-8"))
        return

#         # self.send_header('Content-type','text/html')
#         # self.end_headers()
#         # self.wfile.write(bytes("Hello World !", "utf8"))
#         return
    

# if __name__ == '__main__':
#     from http.server import HTTPServer
#     server = HTTPServer(('localhost', 8080), handler)
#     print('Starting server, use <Ctrl-C> to stop')
#     server.serve_forever()

if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), handler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()
