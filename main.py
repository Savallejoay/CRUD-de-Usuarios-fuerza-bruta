from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel
from typing import Optional

app = FastAPI()

class User(SQLModel):
    id: Optional[int] = None
    username: str
    password: str
    is_active: bool = True

users = [
    User(id=1, username="Santos", password="uide.2026", is_active=True),
    User(id=2, username="James", password="ciberseguridad", is_active=True),
    User(id=3, username="Hollow", password="Knight", is_active=False)
]

@app.post("/users")
def create_user(user: User):
    for u in users:
        if u.username == user.username:
            raise HTTPException(status_code=400, detail="Username ya existe")

    user.id = len(users) + 1
    users.append(user)
    return user

@app.get("/users")
def get_users():
    return users

@app.get("/users/{id}")
def get_user(id: int):
    for user in users:
        if user.id == id:
            return user
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@app.put("/users/{id}")
def update_user(id: int, updated: User):
    for user in users:
        if user.id == id:
            user.username = updated.username
            user.is_active = updated.is_active
            return user
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@app.delete("/users/{id}")
def delete_user(id: int):
    for i, user in enumerate(users):
        if user.id == id:
            users.pop(i)
            return {"message": "Usuario eliminado"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@app.post("/login")
def login(data: User):
    for user in users:
        if user.username == data.username:
            if not user.is_active:
                raise HTTPException(status_code=403, detail="Usuario inactivo")

            if user.password == data.password:
                return {"message": "Login exitoso"}

    raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")