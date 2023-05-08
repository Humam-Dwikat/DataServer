from fastapi import FastAPI

from service import crud_service

app = FastAPI()

app.include_router(router=crud_service.router)
