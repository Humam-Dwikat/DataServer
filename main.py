from fastapi import FastAPI

from service import insert_service

app = FastAPI()

app.include_router(router=insert_service.router)
