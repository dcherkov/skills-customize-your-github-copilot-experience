from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# TODO: Define your data model below.
# Replace the example fields with fields that make sense for your chosen resource.
class Item(BaseModel):
    id: int
    title: str
    author: str

# In-memory storage for items
items = []


# TODO: Task 1 - Create a root GET endpoint that returns a welcome message.
@app.get("/")
def read_root():
    pass


# TODO: Task 2 - Create a POST /items endpoint that adds a new item to the list
# and returns the created item.
@app.post("/items")
def create_item(item: Item):
    pass


# TODO: Task 3 - Create a GET /items endpoint that returns all items.
@app.get("/items")
def get_items():
    pass


# TODO: Task 3 - Create a GET /items/{id} endpoint that returns a single item
# by its ID. Return a 404 error if the item is not found.
@app.get("/items/{id}")
def get_item(id: int):
    pass


# TODO: Task 3 - Create a PUT /items/{id} endpoint that updates an existing item
# by its ID. Return a 404 error if the item is not found.
@app.put("/items/{id}")
def update_item(id: int, updated_item: Item):
    pass


# TODO: Task 3 - Create a DELETE /items/{id} endpoint that removes an item
# by its ID. Return a confirmation message or a 404 error if not found.
@app.delete("/items/{id}")
def delete_item(id: int):
    pass
