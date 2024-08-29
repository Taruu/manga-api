# TEST 3

from fastapi import FastAPI

from .models import create_db_and_tables
from .routers import index

app = FastAPI()

app.include_router(index.router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()