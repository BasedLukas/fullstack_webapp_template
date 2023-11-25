from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, HTTPException, status, Request, Response, Security
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2AuthorizationCodeBearer, HTTPBearer
import os
from dotenv import load_dotenv
import httpx
from urllib.parse import urlencode

from . import schemas, crud
from .database.database import SessionLocal, engine
from .database import models
from .utils import VerifyToken
from .config import get_settings


load_dotenv()
models.Base.metadata.create_all(bind=engine)
token_auth_scheme = HTTPBearer()
app = FastAPI()
auth = VerifyToken()
settings = get_settings()


origins = ["http://localhost:5173"]

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
    return {"message": db_response}


@app.get('/private')
async def private_route(auth_result: str = Security(auth.verify)):
    return auth_result


@app.get("/login")
async def login():
    authorization_url = (
        f"https://{settings.auth0_domain}/authorize"
        f"?response_type=code&client_id={settings.auth0_client_id}"
        f"&redirect_uri={settings.auth0_callback_url}&scope=openid"
    )
    return RedirectResponse(url=authorization_url)

@app.get("/callback")
async def callback(code: str):
    token_url = f"https://{settings.auth0_domain}/oauth/token"
    token_headers = {"content-type": "application/x-www-form-urlencoded"}
    token_data = {
        "grant_type": "authorization_code",
        "client_id": settings.auth0_client_id,
        "client_secret": settings.auth0_client_secret,
        "code": code,
        "redirect_uri": settings.auth0_callback_url,
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(token_url, headers=token_headers, data=token_data)
    response.raise_for_status()
    return response.json()





@app.get("/logout")
async def logout():
    return_to_url = "http://127.0.0.1:8000/"  # The URL where the user should be redirected after logout
    return_to_encoded = urlencode({"returnTo": return_to_url})
    logout_url = f"https://{settings.auth0_domain}/v2/logout?client_id={settings.auth0_client_id}&{return_to_encoded}"
    return RedirectResponse(url=logout_url)