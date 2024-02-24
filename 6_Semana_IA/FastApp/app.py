from fastapi import FastAPI, HTTPException
from uuid import UUID
from typing import List
from models import User, Role

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("0106bfe1-17f4-4d2a-8bfa-c3b75aef1012"),
        first_name="Ana",
        last_name="Maria",
        email="email@gmail.com",
        role=[Role.role_1]
    ),
    User(
        id=UUID("f74c05fe-2519-4ead-b83c-dc74e64e14b7"),
        first_name="Glaucia",
        last_name="Oliveira",
        email="email@gmail.com",
        role=[Role.role_2]
    ),
    User(
        id=UUID("028d7c86-af18-455c-82e1-00ef9dde94b7"),
        first_name="Joyce",
        last_name="Ribeiro",
        email="email@gmail.com",
        role=[Role.role_3]
    ),
]

@app.get("/")
async def root():
    return {"message": "Olá, WoKakers!"}

@app.get("/api/users")
async def get_users():
    return db;

@app.get("/api/users/{id}")
async  def get_users(id: UUID):
    for user in db:
        if user.id == id:
            return user
    return {"message": "Usuário não encontrado!"}

@app.post("/api/users")
async def add_user(user: User):
    """
    Adiciona um usuário na base de dados:
    - **id**: UUID
    - **first_name**: str
    - **last_name**: str
    - **email**:str
    - **role**: List[Role]
    """
    db.append(user)
    return {"id": user.id}


@app.delete("/api/users/{id}")
async def remove_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"Usuário com o id {id} não encontrado!"
    )