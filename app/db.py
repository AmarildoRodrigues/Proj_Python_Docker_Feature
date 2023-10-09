# app/db.py
from pymongo import MongoClient
import os

# Configurar conexão com o MongoDB
MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
MONGO_USERNAME = os.getenv("MONGO_USERNAME", "")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", "")

client = MongoClient(MONGO_HOST, MONGO_PORT, username=MONGO_USERNAME, password=MONGO_PASSWORD)

# Definir o banco de dados e as collections
db = client["fortics"]
users_collection = db["users"]
groups_collection = db["groups"]
