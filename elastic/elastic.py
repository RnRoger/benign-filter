import json
from elasticsearch import Elasticsearch, helpers
ES = Elasticsearch([{'host': 'localhost', 'port': '9200'}])
ES.indices.create(index="test")
docs = json.load(open('./upload.json'))


def index(docs):
    data = []

    for doc in docs:
        print(doc)
        print(doc["entry_name"])
        data.append({
            '_id': int(doc['entry_name']),
            '_index': 'test',
            '_type': 'document',
            '_op_type': 'update',
            'doc': doc,
            'doc_as_upsert': True
        })

        if len(data) >= 100:
            print('Sending batch of 1000 docs to elastic...')
            helpers.bulk(ES, data, request_timeout=30)
            data = []

    helpers.bulk(ES, data)


index(docs)
