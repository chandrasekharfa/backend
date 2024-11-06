from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()
@app.get('/')
def index():
    return {'hello': {'stu': 'chandu'}}
@app.get('/blog')
def blog(limit, published:bool):
    if published:
        return {'data': f'{limit} published blogs'}
    else:
        return {'data': f'{limit} blogs'}

@app.get('/about/{about_id}')
def about(about_id:int):
    return {'about': about_id}

class model(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    price: float
    description: Optional[str]=None
    tax: Optional[float]=None

@app.post('/model/')
def create_model(request: model):
    return request