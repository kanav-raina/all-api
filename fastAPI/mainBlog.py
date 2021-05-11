from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]


@app.get('/')
def index():
    return 'hello kanav raina'

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id:int):                               #by deffault parameters are string you need to specifically assign datatype
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id:int):
    return {'data':{1,2,3,4,5,6}}

@app.get('/blog')
def index(limit=10,published:bool=True,sort:Optional[str]=None):
    return {'data': f'blog list {limit} and published is {published}'}           #http://localhost:8000/blog?limit=100&published=True

@app.post('/blog')
def create_blog(request:Blog):
    return f'blog is created with {request.title}'
