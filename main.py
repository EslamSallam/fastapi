from fastapi import FastAPI, Path, HTTPException, status
from typing import Optional

from Item import Item

app = FastAPI()


# simple Get root Function
@app.get("/")
def home():
    return {"Data": "Test"}


# simple Get About function
@app.get("/about")
def about():
    return {"Data": "About"}


inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "Regular"
    }
}


# Path Params Example
@app.get("/get-item/{item_id}/{name}")
def get_item(item_id: int = Path(None, description="The Id of the item", gt=0, lt=2),
             name: str = None):
    return inventory[item_id]


# Query params Example
# passing test case: http://127.0.0.1:8000/get-by-name/1?name=Milk&test=1
@app.get("/get-by-name/{item_id}")
def get_item(*, item_id: int, name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item name not found")


# simple post request implementation
@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    for id in inventory:
        if item_id == id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Item id already Added")
    inventory[item_id] = item
    return inventory[item_id]
