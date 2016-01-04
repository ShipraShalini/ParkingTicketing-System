from elasticsearch_dsl import DocType, String, Integer


class Slot(DocType):
    slot_no = Integer()
    status = String(index='not_analyzed')
    registration_no = String(index='not_analyzed')
    colour = String(index='not_analyzed')

    class Meta:
        index='parking'
        doc_type = 'slot_info'

