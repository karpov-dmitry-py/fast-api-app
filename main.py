from typing import Optional
from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def get_item(item_id: int, extra: Optional[str] = None, short: bool = False):
    return {'item_id': item_id, 'extra': extra, 'short': short}


@app.get("/models/{model}")
async def get_model(model: ModelName):
    return model


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 5):
    return fake_items_db[skip: skip + limit]
