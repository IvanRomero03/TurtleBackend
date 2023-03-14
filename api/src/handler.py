from http.server import BaseHTTPRequestHandler
from dotenv import load_dotenv
import os
from .RedisDB import RedisDB
#load_dotenv()

# Singleton implementation for handler class
class handlerBase(BaseHTTPRequestHandler):
    def __new__(cls, *args):
        print("new", cls)
        print("new", args)
        if not hasattr(cls, 'instance'):
            cls.instance = super(handlerBase, cls).__new__(cls)
        if not hasattr(cls, 'redis'):
            cls.redis = RedisDB(os.getenv("REDIS_HOST"), os.getenv("REDIS_PORT"), os.getenv("REDIS_DB"), os.getenv("REDIS_USERNAME"), os.getenv("REDIS_PASSWORD"))
        return cls.instance
    
    # def __init__(self) -> None:
    #     #print("init", args)
    #     super().__init__()
        
    #     return
    
