from elasticsearch import Elasticsearch, AsyncElasticsearch


class ClientES:
    """
    Class for get a client from Elasticsearch
    """
    def __init__(self, db_host: str = 'localhost'):
        self.db_host = db_host

    def get_client(self) -> Elasticsearch:
        """
        Get sync client from elasticsearch
        """
        return Elasticsearch(self.db_host)

    def get_async_client(self) -> AsyncElasticsearch:
        """
        Get async client from elasticsearch
        """
        return AsyncElasticsearch(self.db_host)

