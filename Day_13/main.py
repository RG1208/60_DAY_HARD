# Post request
from pydantic import BaseModel,EmailStr #type:ignore
from typing import Optional
from fastapi import FastAPI #type:ignore

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

# Path Parameter
@app.get("/user/{user_id}")
def get_user_by_id(user_id: int):
    return {
        "user_id":user_id
    }

# Query Parameter
@app.get("/user")
def hello(user: User):
    return {
        "Message":"Hello World",
        "User":user
    }