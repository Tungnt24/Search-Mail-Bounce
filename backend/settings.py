from environs import Env

env = Env()
env.read_env() 

class Config:
    HOST = env.str("HOST", default="127.0.0.1")
    PORT = env.int("PORT", default=8080)
    MONGODB_URI = env.str("MONGODB_URI", default="")
    MONGODB_DB = env.str("MONGODB_DB", default="db")
    MONGODB_COLLECTION = env.str("MONGODB_COLLECTION", default="collection")
    USERNAME = env.str("USERNAME", default="")
    PASSWORD = env.str("PASSWORD", default="")
