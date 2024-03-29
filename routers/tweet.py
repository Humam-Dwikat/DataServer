from fastapi import APIRouter

from db_client.client_elasticsearch import ClientES
from repo.repos import Repo
from service.tweet import TweetOperation

router = APIRouter(prefix='/v1/search')

es = ClientES()
repo = Repo(es=es)
client = TweetOperation(repo)


@router.get('/tweets')
async def get_tweet():
    res = await client.get_tweet(index_name='index1')
    return res
