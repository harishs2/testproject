from fastapi import FastAPI,HTTPException
from models import User,Gender,Role
from typing import List
from uuid import UUID


app = FastAPI()

db: List[User] = [
    User(
         id=UUID("c7fab8f7-766c-46a0-8950-aa21038c8bc1"),
         first_name="ram",
         last_name="krishna",
         gender=Gender.male,
         roles=[Role.student]
    ),
    User(
         id=UUID("adf9d914-59ad-4563-8a38-3fa0d860bb13"),
         first_name="shiva",
         last_name="kumar",
         gender=Gender.male,
         roles=[Role.admin, Role.user]
    )
]

@app.get("/")
def root():
    return {"Hello":"earth"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist "

    )





