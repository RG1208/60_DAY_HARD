from fastapi import FastAPI #type:ignore

app = FastAPI()

@app.get("/")
def hello():
    return "Hello World"

@app.get("/bye")
def bye():
    return "Bye"

@app.get("/add")
def add(a:int, b:int):
    return a + b

@app.get("/square")
def square(num:int):
    return num * num

@app.get("/info")
def info():
    return {"name":"Rachit", "age":21, "city":"New Delhi"}