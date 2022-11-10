from  fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional


# Init fastAPI in app
app = FastAPI()

class Item(BaseModel):
    name: str
    price:float
    brand: Optional[str] = None



inventory = {
    1:{
        'name':'Milk',
        'price':'3.99',
        'brand':'regular'
    }
}

@app.get('/get_item/{item_id}')
def get_time(item_id: int =Path(None, description = 'The Id of the item you like' )):
    return inventory[item_id]

@app.get('/get_by_name/{item_id}')
def get_time(*, item_id: int,  name: Optional [str] = None, test: int):
    for item_id in inventory:
        if inventory [item_id] ['name'] == name:
            return inventory [item_id]
    return {'data':'Not found'}


@app.post('/create_item/{item_id}')
def get_time(item_id: int, item : Item):
    if item_id in inventory:
        return {'Error':'Item Already exists'}
    inventory[item_id] = {'name':'item', 'price': item.price, 'brand': item.brand}
    return inventory[item_id]