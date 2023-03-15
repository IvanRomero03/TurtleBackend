from http.server import BaseHTTPRequestHandler
import json
from .src.Parser import Parser
import os
from .src.handlerBase import handlerBase 
from .src.util import randomHash
#from .src.RedisDB import RedisDB
import redis
from dotenv import load_dotenv

load_dotenv()

#redis_db = redis.Redis(host=os.getenv("REDIS_HOST"), port=os.getenv("REDIS_PORT"), db=os.getenv("REDIS_DB"), username=os.getenv("REDIS_USERNAME"), password=os.getenv("REDIS_PASSWORD"))

class handler(handlerBase):
    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        #self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Access-Control-Allow-Methods','GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS')
        print(self.headers)
        print("OPTIONS2")
        self.end_headers()
        return
    def do_GET(self):
        response = 200
        self.send_response(response)
        # check if redis has a ConnectionPool attribute
        # self.send_header('Access-Control-Allow-Origin', '*')
        if not hasattr(self, 'redis'):
            self.redis = redis.Redis(host=os.getenv("REDIS_HOST"), port=os.getenv("REDIS_PORT"), db=os.getenv("REDIS_DB"), username=os.getenv("REDIS_USERNAME"), password=os.getenv("REDIS_PASSWORD"))
        self.send_header('Content-type','text/html')
        self.wfile.write(bytes("Hello World !", "utf8"))
        return
    def do_POST(self):
        # self.send_header('Access-Control-Allow-Origin', '*')
        if not hasattr(self, 'redis'):
            self.redis = redis.Redis(host=os.getenv("REDIS_HOST"), port=os.getenv("REDIS_PORT"), db=os.getenv("REDIS_DB"), username=os.getenv("REDIS_USERNAME"), password=os.getenv("REDIS_PASSWORD"))
        s = self.path
        text = self.rfile.read(int(self.headers['Content-Length'])).decode("utf-8")
        text: dict = json.loads(text)
        textInput = text["text"]
        # if has ["hash"] then get from redis and load query
        parser = Parser()
        if "hash" in text.keys():
            print(text["hash"])
            hashInput = self.redis.get(text["hash"]).decode("utf-8")
            print(hashInput)
            # get from redis
            query = json.loads(hashInput.replace("'", '"'))
            print("query", query)
            for i in query:
                parser.parse(i)
        result = parser.parse(textInput)
        parser.execute()
        hash = randomHash(16)
        #redis_db.set(hash, str(result))
        self.redis.set(hash, str(result))
        svg = parser.getSVG()
        response = 200
        
        self.send_header('Content-type','application/json')
        # self.send_header('Access-Control-Allow-Origin', '*')
        #self.end_headers()
        self.end_headers()
        self.send_response(response)
        jsonResponse = json.dumps({"hash": hash, "svg": svg})
        self.wfile.write(bytes(jsonResponse, "utf-8"))
        
        #self.wfile.write(bytes(jsonResponse, "utf8"))
        print("done")
        return



# class handler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         response = 200
#         self.send_response(response)
#         self.send_header('Content-type','text/html')
#         self.end_headers()
#         self.wfile.write(bytes("Hello World !", "utf8"))
#         return
#     def do_POST(self):
#         s = self.path
#         print(s)
#         # Content-Type: application/json
#         # {"text": "fd 100"}
#         text = self.rfile.read(int(self.headers['Content-Length'])).decode("utf-8")
#         textJson = json.dumps(text)
#         print(text)
#         text = json.loads(text)
#         print(text)
#         textInput = text["text"]
#         print(textInput)
#         print(text)
#         parser = Parser()
#         result = parser.parse(textInput)
#         parser.execute()
#         print(os.getcwd())
#         # print tree 
#         print(os.listdir())
#         #create empty file
#         #open("/temp/temp.svg", "w").close()
#         svg = parser.getSVG()

#         response = 200
#         self.send_response(response)
#         # send the svg file
#         self.send_header('Content-type','image/svg+xml')
#         self.end_headers()
#         self.wfile.write(svg.encode("utf-8"))
#         return

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
