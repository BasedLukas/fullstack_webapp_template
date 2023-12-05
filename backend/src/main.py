from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import logging

from .database.database import engine
from .database import models
from .config import get_settings
from .routes import router

settings = get_settings()
log = logging.getLogger(__name__)
log.setLevel(settings.log_level)

models.Base.metadata.create_all(bind=engine)
origins = settings.origins
origins = origins.split(',')
print(origins)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)

