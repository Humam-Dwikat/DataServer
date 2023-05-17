from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

from rendering.render_mapping import render_mapping

host = 'http://localhost:9200'

es = Elasticsearch(hosts=host)

mappings = render_mapping(path='/home/humam/Simulate Server/migration/index_001.tmpl',
                          number_of_shards=1,
                          number_of_replicas=2)

es.indices.create(index='insert_trying', mappings=mappings)

# content = open("/home/humam/Downloads/20221101000000.json", 'r')
#
#
# def stream():
#     for line in content:
#         yield {
#             "_index": "mywords",
#             "data": line
#         }
#
#
# bulk(es, stream())

# print(result)
# content = open("/home/humam/Downloads/20221101000000.json")
# print(content.read())
# result = es.index(index=index_name, document=doc)

