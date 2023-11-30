from typing import List
from fastapi import FastAPI, Depends, HTTPException, status, Request, Response, Security, APIRouter
from fastapi.security import OAuth2AuthorizationCodeBearer, HTTPBearer
from fastapi.responses import RedirectResponse
import logging

from .database.database import SessionLocal, get_db
from .auth import login, logout, callback
from .config import get_settings
from . import schemas, crud
from .utils import VerifyToken


router = APIRouter()
settings = get_settings()
auth = VerifyToken()
token_auth_scheme = HTTPBearer()



@router.get("/", response_model=schemas.MessageResponse)
async def get_(db: SessionLocal = Depends(get_db)):
    db_msg = await crud.get_message(db=db)
    if db_msg:
        return {"id": db_msg.id, "message": db_msg.message}
    else:
        raise HTTPException(status_code=404, detail="Message not found")


@router.post("/", response_model=schemas.MessageCreate)
async def post_(message: schemas.MessageCreate, db: SessionLocal = Depends(get_db)):
    db_response =  await crud.create_message(db=db, message=message)
    print(db_response)
    return {"message": db_response}


@router.get('/private')
async def private_route(auth_result: str = Security(auth.verify)):
    return auth_result


@router.get("/login")
async def login_()-> RedirectResponse:
    return await login()


@router.get("/callback")
async def callback_(code: str):
    return await callback(code)


@router.get("/logout")
async def logout_() -> RedirectResponse:
    return await logout()