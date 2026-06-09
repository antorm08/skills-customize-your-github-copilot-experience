from typing import Optional, Dict
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import uvicorn

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

app = FastAPI()

_items: Dict[int, Item] = {}
_next_id = 1

@app.get("/items")
def list_items():
    return [{"id": i, **_items[i].dict()} for i in _items]

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in _items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item no encontrado")
    return {"id": item_id, **_items[item_id].dict()}

@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    global _next_id
    item_id = _next_id
    _items[item_id] = item
    _next_id += 1
    return {"id": item_id, **item.dict()}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in _items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item no encontrado")
    _items[item_id] = item
    return {"id": item_id, **item.dict()}

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    if item_id not in _items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item no encontrado")
    del _items[item_id]
    return None

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
