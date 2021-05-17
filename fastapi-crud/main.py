from typing import Optional
from fastapi import FastAPI,Depends,status,Response,HTTPException
from database import engine,Base,get_db
from sqlalchemy.orm import Session 
from schemas import Blog,ShowBlog
import models

app = FastAPI()

models.Base.metadata.create_all(engine)


#CRUD
@app.post('/blog',status_code=status.HTTP_201_CREATED,tags=['blogs'])
def create(request:Blog,db:Session=Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog/{id}',status_code=200,response_model=ShowBlog,tags=['blogs'])
def show(id,response:Response,db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Blog with the id {id} is not available '
        )
    return blog

@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['blogs'])
def destory(id,db:Session = Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Blog with the id {id} is not available '
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=['blogs'])
def update(id, request:Blog,db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Blog with the id {id} is not available '
        )
    blog.update(request)
    db.commit()

    return 'updated'