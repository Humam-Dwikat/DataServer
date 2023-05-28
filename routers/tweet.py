from pathlib import Path

from elasticsearch import Elasticsearch
from fastapi import APIRouter

from db_client.client_elasticsearch import ClientES
from db_client.operation_es import OperationES
from confing.configDB import Config
from repo.repos import Repo
from service.tweet import TweetOperation

router = APIRouter(prefix='/v1/insert')

es = ClientES()
operation_es = OperationES(es)
repo = Repo(es=operation_es)
client = TweetOperation(repo)


@router.get('/alltweets')
def get_tweet(index_name: str):
    return client.get_tweet(index_name=index_name)
