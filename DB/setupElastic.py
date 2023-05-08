import asyncio
from elasticsearch import AsyncElasticsearch

es = AsyncElasticsearch([{'host': 'localhost', 'port': 9200}])

index_name = 'test_index'
doc_type = 'test_doc_type'
document = {"id": "1234",
            "title": "Example Document",
            "body": "This is an example document that contains some text.",
            "author": {
                "name": "John Doe",
                "email": "john.doe@example.com"
            },
            "tags": ["example", "document", "search"]
            }

es.index(index=index_name, doc_type=doc_type, document=document)
