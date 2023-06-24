from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def connect_to_mongodb():
    try:
        client = MongoClient("mongodb+srv://User:user@mongodb1.dz8ee6z.mongodb.net/BluckBoster")
        db = client.BluckBoster
        print("DB RUNNING")
    except ConnectionFailure as e:
        print("Error de Conexion", e)
    return db
