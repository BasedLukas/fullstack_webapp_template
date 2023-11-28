from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, HTTPException, status, Request, Response, Security
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2AuthorizationCodeBearer, HTTPBearer
import os
import httpx
from urllib.parse import urlencode
import logging

from . import schemas, crud
from .database.database import SessionLocal, engine
from .database import models
from .auth import login, logout, callback
from .utils import VerifyToken
from .config import get_settings

settings = get_settings()
log = logging.getLogger(__name__)
log.setLevel(settings.log_level)

models.Base.metadata.create_all(bind=engine)
token_auth_scheme = HTTPBearer()
app = FastAPI()
auth = VerifyToken()




origins = [settings.origins]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_model=schemas.MessageResponse)
async def get_(db: SessionLocal = Depends(get_db)):
    db_msg = crud.get_message(db=db)
    if db_msg:
        return {"id": db_msg.id, "message": db_msg.message}
    else:
        raise HTTPException(status_code=404, detail="Message not found")


@app.post("/", response_model=schemas.MessageCreate)
async def post_(message: schemas.MessageCreate, db: SessionLocal = Depends(get_db)):
    db_response = crud.create_message(db=db, message=message)
    print(db_response)
    return {"message": db_response}


@app.get('/private')
async def private_route(auth_result: str = Security(auth.verify)):
    return auth_result


@app.get("/login")
async def login_():
    return await login()


@app.get("/callback")
async def callback_(code: str):
    return await callback(code)



@app.get("/logout")
async def logout_():
    return await logout()