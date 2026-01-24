from fastapi import FastAPI
from app.database import engine, Base
from app import models
from app.auth import router as auth_router
from app.sync import router as vault_router

app = FastAPI(title="Password Manager Backend")

models.Base.metadata.create_all(bind=engine)

app.include_router(auth_router)

app.include_router(vault_router)

@app.get("/")
def root(data:int , name:str):
    if data>20:
        return{name,"fail"}
    else:
        return{name,"pass"}  