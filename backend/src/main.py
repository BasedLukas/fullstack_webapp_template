from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, HTTPException, status, Request, Response
from fastapi.security import OAuth2AuthorizationCodeBearer
import os
from dotenv import load_dotenv
from . import schemas, crud
from .database.database import SessionLocal, engine
from .database import models
load_dotenv()
models.Base.metadata.create_all(bind=engine)
app = FastAPI()


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

