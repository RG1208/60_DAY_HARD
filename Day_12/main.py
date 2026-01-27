from pydantic import BaseModel,EmailStr #type:ignore
from typing import Optional
from fastapi import FastAPI #type:ignore

app = FastAPI()

@app.get("/")
def hello():
    return "Hello World"
class User (BaseModel):
    name: str
    email: EmailStr
    age: int
    phone: Optional[str]=None

@app.post("/user")
def add_user(user: User):
    return{
        "Message":"user added successfully",
        "Data":user
    }

