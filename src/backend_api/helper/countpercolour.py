from elasticsearch import Elasticsearch

INDEX = 'parking'

def count_per_colour():
    body ={"aggs" : {
        "count_per_colour": {
          "terms": {"field": "colour"}
          }
        }
      }

    es = Elasticsearch(index=INDEX)
    res = es.search(index=INDEX, body=body)

    return res['aggregations']['count_per_colour']['buckets']



