import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://admin:adminpassword@localhost:27017")

client = pymongo.MongoClient(MONGO_URI)
db = client["scientists_db"]
collection = db["scientists"]

def save_to_db(data):
    collection.insert_one(data)

