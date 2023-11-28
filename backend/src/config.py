from functools import lru_cache

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    auth0_domain: str
    auth0_api_audience: str
    auth0_issuer: str
    auth0_algorithms: str
    auth0_client_id: str
    auth0_callback_url: str
    auth0_client_secret: str

    # frontend url
    origins: str 

    #database
    username :str
    password :str
    host :str
    port :str # Default PostgreSQL port
    database :str  # The database name

    # other
    log_level: str 

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()