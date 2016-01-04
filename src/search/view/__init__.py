from src.models.model import Slot
from elasticsearch_dsl.connections import connections

# initializing
connections.create_connection(hosts=['localhost'])
Slot.init()