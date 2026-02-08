from typing import List
from pydantic import BaseSettings # type: ignore
from pydantic  import field_validator # type: ignore


class Settings(BaseSettings):
    API_PREFIX: str = "/api"
    DEGUG: bool = False

    DATABASE_URL: str

    ALLOWED_ORIGINS: List[str] = ""

    OPENAI_API_KEY: str

    @field_validator("ALLOWED_ORIGINS")
    def parse_allowed_origins(cls, v: str) -> List[str]:
        return [origin.strip() for origin in v.split(",") if origin.strip()]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()