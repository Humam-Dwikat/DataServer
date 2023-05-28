import elasticsearch
from elasticsearch import Elasticsearch

from db_client.client_elasticsearch import ClientES
from db_client.operation_es import OperationES


class Repo:
    def __init__(self, es: OperationES):
        self.es = es

    # make it separate from this file
    def index_document(self,
                       index_name: str,
                       path_file: str = "/home/humam/Downloads/20221101000000.json"):
        try:
            return self.es.index_document(index_name=index_name, path_file=path_file)
        except elasticsearch.ConnectionError as error:
            raise error

    # make it separate from this file
    def create_index(self, index_name: str,
                     number_of_shards: int,
                     number_of_replicas: int,
                     path: str = '/home/humam/Simulate Server/migration/index_001.tmpl'):
        try:
            return self.es.create_index(index_name=index_name,
                                        number_of_shards=number_of_shards,
                                        number_of_replicas=number_of_replicas,
                                        path=path)
        except Exception:
            pass

    def get_tweet(self, index_name: str):
        return self.es.get_tweet(index_name=index_name)
