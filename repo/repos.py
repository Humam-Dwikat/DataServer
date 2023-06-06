from db_client.client_elasticsearch import ClientES


class Repo:
    """
    class for the operation that effect in the database
    """
    def __init__(self, es: ClientES):
        self.es = es

    def get_tweet(self, index_name: str):
        query = {"query": {"match_all": {}}}
        client = self.es.get_client()
        res = client.search(index=index_name, body=query, scroll='3m')
        return res
