from pydantic import BaseModel #type:ignore
from typing import Optional,List
from fastapi import FastAPI #type:ignore


app = FastAPI()

class Tea(BaseModel):
    name: str
    id:int
    origin:str

teas:List[Tea]=[]

@app.get("/")
def general():
    return("Hello, your api is working")

@app.get("/teas")
def get_all_teas():
    return(teas)

@app.post("/teas")
def add_tea(tea:Tea):
    teas.append(tea)
    return (teas)

@app.put("/teas/{tea_id}")
def update_tea(tea_id:int,update_tea:Tea):
    for idx,tea in enumerate(teas):
        if tea.id == tea_id:
            teas[idx]=update_tea
            return update_tea
    return {"error":"tea not found"}

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id:int,updates_tea:Tea):
    for idx,tea in enumerate(teas):
        if tea.id == tea_id:
            deleted = teas.pop(idx)
            return deleted
    return {"error":"tea not found"}