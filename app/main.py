from fastapi import FastAPI
from fastapi.params import Depends
# from requests import Session
from sqlalchemy.orm import Session
from sqlalchemy import Engine

from app import models, schemas
from .database import Base, SessionLocal, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




# simple route for home page
@app.get("/")
def read_api(db:Session = Depends(get_db) ):
    return db.query(models.User).all()

@app.post("/users/",response_model=schemas.UserResponse)
def create_user(user:schemas.UserCreate, db: Session = Depends(get_db)):

    hashed_pw = "fakehash_" + user.password
    # user_model = models.User()
    # user_model.name = user.name
    # user_model.email = user.email
    # user_model.hashed_password = user.has

    user_model = models.User(
        name=user.name,
        email=user.email,
        hashed_password=hashed_pw
    )
    
    db.add(user_model)
    db.commit()

    return user_model


# route for health check
@app.get("/health")
def health_check():
    return {"status": "healthy"}




