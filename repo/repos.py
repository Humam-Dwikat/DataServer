from db_client.client_elasticsearch import ClientES


class Repo:
    """
    class for the operation that effect in the database
    """

    def __init__(self, es: ClientES):
        self.es = es

    async def get_tweet(self, index_name: str):
        query = {
            "query": {
                "match_all": {}
            },
            "size": 20,
            "from": 0
        }
        client = self.es.get_async_client()
        res = await client.search(index=index_name, body=query)

        return res
