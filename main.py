import uvicorn
from elasticsearch import Elasticsearch
from fastapi import FastAPI

from db_client.client_elasticsearch import ClientES
from db_client.operation_es import OperationES
from repo.repos import Repo
from routers import tweet
from service.tweet import TweetOperation

app = FastAPI()
es = Elasticsearch()
app.include_router(router=tweet.router)


if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0')
