import json

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

from db_client.client_elasticsearch import ClientES
from confing.configDB import Config
from exception.ES_exception import IndexExists
from rendering.render_mapping import read_file, render_mapping

config = Config()


def read_file_line_by_line(path: str):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            content = file
            for line in content:
                try:
                    line = json.loads(line)
                    yield line
                except Exception:
                    continue
    except OSError as error:
        raise error


def stream(path: str, index_name: str):
    # content = read_file_line_by_line(path=path)
    for line in read_file_line_by_line(path):
        # parse_tweet = json.loads(line)
        try:
            yield {
                "_index": index_name,
                "_id": line['id_str'],
                "_source": line
            }
        except Exception:
            continue


class OperationES:
    def __init__(self, es: ClientES):
        self.client = es

    def index_document(self, index_name: str, path_file: str = "/home/humam/Downloads/20221101000000.json"):
        """
        index the document in elasticsearch
        """
        client = self.client.get_client()
        data = stream(index_name=index_name, path=path_file)

        response = bulk(client=client, actions=data, stats_only=True, ignore_status=400)
        return response

    def create_index(self,
                     index_name: str,
                     number_of_shards: int,
                     number_of_replicas: int,
                     path: str = '/home/humam/Simulate Server/migration/index_001.tmpl'):
        client = self.client.get_client()
        if client.indices.exists(index=index_name):
            raise IndexExists('Index already exists')

        else:
            mapping = render_mapping(number_of_shards=number_of_shards,
                                     number_of_replicas=number_of_replicas,
                                     path=path)
            # mappings = json.loads(mapping)
            index = client.indices.create(index=index_name, mappings=mapping)

            return index

    def get_tweet(self, index_name: str):
        client = self.client.get_client()
        res = client.get(index=index_name, id='1587232917977079808')
        return res
