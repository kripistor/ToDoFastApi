import os

from dotenv import load_dotenv
from pydantic.v1 import BaseSettings

load_dotenv()


class Config(BaseSettings):
    postgres_dsn = os.getenv('POSTGRES_DSN')

    class Config:
        env_file = '../env'


config = Config()
