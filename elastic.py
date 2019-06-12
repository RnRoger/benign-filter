import json
import sys
from elasticsearch import Elasticsearch, helpers
ES = Elasticsearch([{'host': 'localhost', 'port': '9200'}])
try:
    ES.indices.create(index=f'{sys.argv[1]}')
except:
    pass

docs = json.load(open(f'./{sys.argv[2]}'))


def index(docs):
    data = []
    count = 0
    for doc in docs:
        data.append({
            '_id': doc['ID'],
            '_index': sys.argv[1],
            '_type': 'document',
            '_op_type': 'update',
            'doc': doc,
            'doc_as_upsert': True,
            'NAME': doc['NAME'],
            'AF': doc['Allele frequency'],
            'REF': doc['REF'],
            'POS': doc['POS'],
            "most_severe_consequence" : doc['most_severe_consequence'],
            "clinical_significance" : doc['clinical_significance']
        })

        if len(data) >= 10:
            print('Sending batch of 10 docs to elastic...')
            helpers.bulk(ES, data, request_timeout=30)
            data = []
        
        count += 1
    helpers.bulk(ES, data)
    with open(f"data/{sys.argv[1]}done.txt", "w") as outfile:
        outfile.write("gj")


index(docs)
