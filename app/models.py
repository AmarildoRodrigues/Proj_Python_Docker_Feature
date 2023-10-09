from typing import List
# Esta função simula a obtenção de usuários do banco de dados
from app.db import get_users_collection

def get_users() -> List[str]:
    users = get_users_collection().find()
    return [user["name"] for user in users]


# Esta função simula a obtenção de grupos do banco de dados
def get_groups() -> List[str]:
    return ["group1", "group2", "group3"]
