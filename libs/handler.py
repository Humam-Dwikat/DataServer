import json

from elasticsearch.helpers import bulk

from db_client.client_elasticsearch import ClientES
from confing.configDB import Config
from exception.ES_exception import IndexExists
from rendering.render_mapping import render_mapping

config = Config.get_instance()


def read_file_line_by_line(path: str):
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                line = json.loads(line)
                yield line
            except Exception as err:
                print(err)
                continue


def stream(path: str, index_name: str):
    for line in read_file_line_by_line(path):
        parse_tweet = json.dumps(line)
        # object1 = dict(line)
        try:
            yield {"_index": index_name,
                   "_id": line["id_str"],
                   "_source": parse_tweet
                   }
        except Exception:
            continue


class CIOperationES:
    """
    This class for create index and index
    document in the index of elasticsearch


    """

    def __init__(self, es: ClientES):
        self.client = es

    def index_document(
            self,
            index_name: str,
            path_file: str = "/home/humam/Downloads/20221101000000.json"):
        """
        index the document in elasticsearch
        """
        client = self.client.get_client()
        data = stream(index_name=index_name, path=path_file)
        response = bulk(client=client, actions=data, ignore_status=400)
        return response

    def create_index(self,
                     index_name: str,
                     number_of_shards: int,
                     number_of_replicas: int,
                     path: str = '/home/humam/SimulateServer/migration/index_001.tmpl'):

        client = self.client.get_client()
        if client.indices.exists(index=index_name):
            raise IndexExists('Index already exists')

        else:
            mapping = render_mapping(number_of_shards=number_of_shards,
                                     number_of_replicas=number_of_replicas,
                                     path=path)
            # mappings = json.loads(mapping)
            setting = {
                "index": {
                    "number_of_replicas": number_of_replicas,
                    "number_of_shards": number_of_shards
                }
            }
            index = client.indices.create(index=index_name, mappings=mapping, settings=setting)

        return index
