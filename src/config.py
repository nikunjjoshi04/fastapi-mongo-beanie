from pydantic import BaseSettings


class Settings(BaseSettings):
    mongo_username: str
    mongo_password: str
    # mongo_database: str
    mongo_host: str
    mongo_port: str
    mongo_config_url: str


settings = Settings()
