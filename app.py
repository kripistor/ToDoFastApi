from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import Session
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from todo.configreader import config

from todo.database.models import Task

app = FastAPI()

app.mount('/static', StaticFiles(directory='todo/static/'), name='static')
templates = Jinja2Templates(directory='todo/template')

from todo.routes import home
