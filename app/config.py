from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    bot_token: str
    database_url: str
    itad_api_key: str
    check_interval_hours: int = 3

    class Config:
        env_file = ".env"


settings = Settings()
