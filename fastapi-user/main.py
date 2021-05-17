from typing import Optional
from fastapi import FastAPI,Depends,status,Response,HTTPException
from database import engine,Base,get_db
from sqlalchemy.orm import Session 
from schemas import User,ShowUser
import models
import hashing
app = FastAPI()

models.Base.metadata.create_all(engine)

@app.post('/user',response_model=ShowUser,tags=['users'])
def create_user(request:User,db:Session=Depends(get_db)):
    new_user=models.User(name=request.name,email=request.email,password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get('/user/{id}',response_model=ShowUser,tags=['users'])#response model se specify krte ho ke response main kaunsi fields ayengi
def create_user(id,response:Response,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with the id {id} is not available '
        )
    return user