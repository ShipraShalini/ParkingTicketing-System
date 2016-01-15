from src.models.model import Slot
from elasticsearch_dsl.connections import connections

# initializing
connections.create_connection(hosts=['localhost'])
Slot.init()

# from elasticsearch import Elasticsearch
# from elasticsearch_dsl import Search
# es = Elasticsearch(index='parking')
# s = Search(es