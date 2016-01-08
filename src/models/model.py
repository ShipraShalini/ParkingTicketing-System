from common.constants import *
from elasticsearch_dsl import DocType, String, Integer


class Slot(DocType):
    slot_no = Integer()
    status = String(index=ANALYSER)
    registration_no = String(index=ANALYSER)
    colour = String(index=ANALYSER)

    class Meta:
        index=INDEX
        doc_type = DOC_TYPE

