from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    DATABASE_URL: str
    # SECRET_KEY: str = "fallback-secret"
    DEBUG: bool = False
    APP_NAME: str = "Employee Attendance API"

@lru_cache()
def get_settings() -> Settings:
    return Settings()