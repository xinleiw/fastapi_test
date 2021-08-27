

from fastapi import FastAPI

from app.api import api_router
from app.lib.init_db import init_database
init_database()

print("aaaaaaaaaa")
app = FastAPI()
app.include_router(api_router, prefix="/api")
