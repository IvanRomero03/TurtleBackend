from http.server import BaseHTTPRequestHandler
import json
from Parser import Parser
import os
from RedisDB import RedisDB
from dotenv import load_dotenv

load_dotenv()

# Singleton implementation for handler class
class handler(BaseHTTPRequestHandler):
    def __new__(cls, *args) -> BaseHTTPRequestHandler:
        print("new", cls)
        print("new", args)
        if not hasattr(cls, 'instance'):
            cls.instance = super(handler, cls).__new__(cls)
        if not hasattr(cls, 'redis'):
            cls.redis = RedisDB(os.getenv("REDIS_HOST"), os.getenv("REDIS_PORT"), os.getenv("REDIS_DB"), os.getenv("REDIS_USERNAME"), os.getenv("REDIS_PASSWORD"))
        return cls.instance
    
    # def __init__(self) -> None:
    #     #print("init", args)
    #     super().__init__()
        
    #     return
    
