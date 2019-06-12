from elasticsearch import Elasticsearch, helpers
import sys

ES = Elasticsearch([{'host': 'localhost', 'port': '9200'}])
 

res = ES.search(index=sys.argv[1], body={"size":666, "query": {"match_all": {}}})

with open('data/'+sys.argv[1]+'report.html','w') as outfile:
    outfile.write("<table style='width:100%'>")
    outfile.write("""<tr>
                        <th>ID</th>
                        <th>CHROM</th>
                        <th>POS</th>
                        <th>REF</th>
                        <th>NAME</th>
                        <th>Allele Frequency</th>
                        <th>Most Severe Consequence</th>
                        <th>Clinical Significance</th>
                        </tr>""")
    outfile.write("<tr>")
    for hit in res['hits']['hits']:
        outfile.write('<tr>')
        for result in hit['_source'].values():
            outfile.write(f"<th>{str(result)}</th>")
        outfile.write('</tr>')
    outfile.write("</tr><br>")
    outfile.write(f"Total hits: {len(res['hits']['hits'])}")
    