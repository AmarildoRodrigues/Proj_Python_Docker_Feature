from fastapi import FastAPI
from app.models import get_users, get_groups
import os

app = FastAPI()

@app.get("/users")
def read_users():
    return get_users()

@app.get("/groups")
def read_groups():
    return get_groups()

if __name__ == "__main__":
    host = os.getenv("MONGODB_HOST", "localhost")
    port = os.getenv("MONGODB_PORT", 27017)
    uvicorn.run(app, host=host, port=8000)
