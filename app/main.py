# app/main.py
from fastapi import FastAPI
from app.db import users_collection, groups_collection
import logging

# Configurar o logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/users")
def get_users():
    users = list(users_collection.find())
    return users

@app.get("/groups")
def get_groups():
    groups = list(groups_collection.find())
    return groups
