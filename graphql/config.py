import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    POSTGRES_USER: str = "ApplicationHub"
    POSTGRES_PASSWORD: str = "ApplicationHub"
    POSTGRES_SERVER: str = "applicaion-hub.cy89bcs5bmiv.us-east-2.rds.amazonaws.com"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "postgres"

settings = Settings()