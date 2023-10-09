from pymongo import MongoClient
import os

def get_db():
    host = os.getenv("MONGODB_HOST", "localhost")
    port = os.getenv("MONGODB_PORT", 27017)
    client = MongoClient(f"mongodb://{host}:{port}")
    return client.fortics

def get_users_collection():
    db = get_db()
    return db.users

def get_groups_collection():
    db = get_db()
    return db.groups
