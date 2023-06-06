import uvicorn
from elasticsearch import Elasticsearch
from fastapi import FastAPI

from routers import tweet

app = FastAPI()
es = Elasticsearch()
app.include_router(router=tweet.router)


if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0')
