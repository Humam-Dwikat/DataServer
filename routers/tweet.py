from fastapi import APIRouter

from db_client.client_elasticsearch import ClientES
from repo.repos import Repo
from service.tweet import TweetOperation

router = APIRouter(prefix='/v1/get')

es = ClientES()
repo = Repo(es=es)
client = TweetOperation(repo)


@router.get('/alltweets')
def get_tweet():
    res = client.get_tweet(index_name='index1')
    return res
