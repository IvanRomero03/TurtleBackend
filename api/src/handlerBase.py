from http.server import BaseHTTPRequestHandler
#from dotenv import load_dotenv
import os
# from .RedisDB import RedisDB
#load_dotenv()

import redis
import json
try:
    class RedisDB:
        def __init__(self, host, port, db, username, password):
            self.host = host
            self.port = port
            self.db = db
            self.username = username
            self.password = password
            self.pool = redis.ConnectionPool(host=self.host, port=self.port, db=self.db, username=self.username, password=self.password)
            
        def set(self, key, value) -> None:
            r = redis.Redis(connection_pool=self.pool)
            r.set(key, value)

        def get(self, key) -> (bytes | None):
            r = redis.Redis(connection_pool=self.pool)
            return r.get(key)
        
        def delete(self, key) -> None:
            r = redis.Redis(connection_pool=self.pool)
            r.delete(key)

        def exists(self, key) -> bool:
            r = redis.Redis(connection_pool=self.pool)
            return r.exists(key)
        
        def keys(self) -> list[bytes]:
            r = redis.Redis(connection_pool=self.pool)
            return r.keys()
        
        def flush(self) -> None:
            r = redis.Redis(connection_pool=self.pool)
            r.flushdb()

        def get_all(self) -> dict:
            return {key.decode("utf-8"): self.get(key).decode("utf-8") for key in self.keys()}
        
        def get_all_json(self) -> str:
            return json.dumps(self.get_all())

except Exception as e:
    print(e)

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
    
