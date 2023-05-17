from fastapi import FastAPI

from service import indexing

app = FastAPI()

app.include_router(router=indexing.router)
