from db_client.operation_es import OperationES
from repo.repos import Repo


class TweetOperation:
    def __init__(self, repo: Repo):
        self.repo = repo

    def index_document(self, index_name: str,
                       path: str = "/home/humam/Downloads/20221101000000.json"):
        return self.repo.index_document(index_name=index_name, path_file=path)

    def create_index(self, index_name: str,
                     number_of_shards: int,
                     number_of_replicas: int,
                     path: str = '/home/humam/Simulate Server/migration/index_001.tmpl'):
        """
        this function for create a new index
        """
        return self.repo.create_index(index_name=index_name,
                                      number_of_shards=number_of_shards,
                                      number_of_replicas=number_of_replicas,
                                      path=path)

    def get_tweet(self, index_name: str):
        return self.repo.get_tweet(index_name=index_name)
