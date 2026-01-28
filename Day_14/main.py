# Post request
from pydantic import BaseModel,EmailStr #type:ignore
from typing import Optional
from fastapi import FastAPI #type:ignore
from fastapi import HTTPException #type:ignore

app = FastAPI()

class User(BaseModel):
    name: str
    email: EmailStr
    user_id: int

# Post request
@app.post("/user")
def get_user(user: User):
    return {
        "name":user.name,
        "email":user.email,
        "user_id": user.user_id
    }

@app.get("/users/{user_id}")
def get_user(user_id: int):
    users = {1: "Rachit"}

    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {"user": users[user_id]}
