from pyexpat.errors import messages

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
import uvicorn

app = FastAPI()

class CreateUser(BaseModel):
    email: EmailStr

@app.get("/")
def hello_index():
    return  {
        "Hello index",
    }

@app.get("/hello/")
def hello(name:str = "World"):
    name = name.strip().title()
    return {"message": f"Hello {name}!"}


@app.post("/users/")
def create_user(user: CreateUser):
    return  {
        "message": "success",
        "email": user.email,
    }


@app.get("/items/")
def list_items():
    return [
        "Items1",
        "Items2",
        "Items3"
    ]


@app.get("/items/latest/")
def get_latest_items():
    return {"item": {"id": "0", "name": "latest"}}



@app.get("/items/{item_id}/")
def get_item_by_id(item_id: int):
    return  {
        "item":{
            "id": item_id,
        },
    }




if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
