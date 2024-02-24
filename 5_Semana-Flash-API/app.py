from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Role
from uuid import UUID
app = FastAPI()

db: List[User] = [
    User(
        id=UUID("06640486-fcaf-4e90-a95b-6c3af1f58fa2"),
        first_name="Ana",
        last_name="Maria",
        email="email@gmail.com",
        role=[Role.role_1]
    ),

    User(
        id=UUID("4d34c0f0-2898-4882-ab64-7df926a31e6c"),
        first_name="Cintia",
        last_name="Zanoni",
        email="email@gmail.com",
        role=[Role.role_2]
    ),
    User(
        id=UUID("7593cf72-486b-44ba-82ae-1e6611708dbd"),
        first_name="Camila",
        last_name="Silva",
        email="email@gmail.com",
        role=[Role.role_2]
    )
]

@app.get("/")
async def root():
    return {"message": "Olá, WomaKers!"}


@app.get("/api/users")
async def get_users():
    return db;

@app.get("/api/users/{user_id}") 
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return user
    return {"message":"Usuário não encontrado!"}

@app.post("/api/users")
async def add_user(user: User):
    db.append(user)
    return{"id":user.id}

@app.delete("/api/users/{id}")
async def remove_users(id:UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"Usuário com o id {id} não encontrado!"
    )


@app.post("/api/users")
async def add_user(user: User):
    """
      Adiciona um usuário na base de dados:
    - **id**: UUID
    - **first_name**: string
    - **last_name**: string
    - **email**: string
    - **role**: Role
    """ 
    db.append(user)