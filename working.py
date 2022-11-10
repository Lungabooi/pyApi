from  fastapi import FastAPI, Path, HTTPExpection, status
from pydantic import BaseModel
from typing import Optional


# Init fastAPI in app
app = FastAPI()

class Item(BaseModel):
    name: str
    price:float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name:Optional [str] = None
    price:float = None
    brand: Optional [str] = None

inventory = {
    1:{
        'name':'Milk',
        'price':'3.99',
        'brand':'regular'
    },
    2:{
        'name':'Bread',
        'price':'9.00',
        'brand':'Sasko'
    }
}

@app.get('/get_items')
def get_all_times():
        return inventory 
  




@app.get('/get_item/{item_id}')
def get_item_by_id(item_id: int =Path(None, description = 'The Id of the item you like' )):
    return inventory[item_id]

@app.get('/get_by_name/{item_id}')
def get_item_name_using_id(*, item_id: int,  name: Optional [str] = None):
    for item_id in inventory:
        if inventory [item_id] ['name'] == name:
            return inventory [item_id]
    raise HTTPExpection(status_code=404, detail='Item name not found')



@app.post('/create_item/{item_id}')
def create_an_item(item_id: int, item : Item):
    if item_id in inventory:
        raise HTTPExpection(status_code=404, detail='Item already exists')
    inventory[item_id] = {'name':'item', 'price': item.price, 'brand': item.brand}
    return inventory[item_id]

@app.put('/update_item/{item_id}')
def update_item(item_id: int, item:UpdateItem):
    if item_id not in inventory: 
            return {'Error: Item Id does not exist.'}
    inventory[item_id].update(item)
   
@app.delete('/delete_item')
def delete_item(item_id: int ):
    if item_id not in inventory:
       raise HTTPExpection(status_code=404, detail='Item Id does not exists')
    del inventory[item_id]
    return {'Success':'item have been deleted'}