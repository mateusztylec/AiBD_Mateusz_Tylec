from pydantic import BaseSettings


class settings(BaseSettings):
    haslo: str
    host: str
    nazwa_bazy: str
    login: str
    port: str

    class Config():
        env_file = '.env'

settings = settings()