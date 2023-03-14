import redis
import json
import dotenv
import os

class RedisDB:
    def __init__(self, host, port, db, username, password) -> None:
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
    
    
# if __name__ == "__main__":
#     dotenv.load_dotenv()
#     host = os.getenv("REDIS_HOST")
#     port = os.getenv("REDIS_PORT")
#     db = os.getenv("REDIS_DB")
#     username = os.getenv("REDIS_USERNAME")
#     password = os.getenv("REDIS_PASSWORD")
#     redisDB = RedisDB(host, port, db, username, password)
#     redisDB.set("test", "test")
#     print(redisDB.keys())
#     print(redisDB.get("test"))
#     print(redisDB.get_all_json())
#     pass
