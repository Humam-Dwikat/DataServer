from elasticsearch import Elasticsearch, AsyncElasticsearch


class ClientES:
    def __init__(self, db_host: str = 'localhost'):
        self.db_host = db_host

    def get_client(self) -> Elasticsearch:
        return Elasticsearch(self.db_host)

    def get_async_client(self) -> AsyncElasticsearch:
        return AsyncElasticsearch(self.db_host)

