from fastapi import FastAPI
from app.database import engine, Base
from app import models
from app.auth import router as auth_router
from app.vault import router as vault_router
from app.sync import router as sync_router

app = FastAPI(title="Password Manager Backend")

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)

app.include_router(vault_router)

app.include_router(sync_router)

@app.get("/")
def root():
    return {"message": "API is running"}

      