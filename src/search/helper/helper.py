from src.models.model import Slot
from common.constants import *

ITEM_INDEX='parking'

def create_query():
    d = {
        "aggs" : {
            "min_slot": {
                "min" : { "field" : SLOT_NO}
            }
        }
}


def assign_slot():
    s = Slot.search().sort(SLOT_NO)
    res = s.filter("term", status=STATUS_FREE).execute()[:1]
    if res:
        return res[0].slot_no
    else:
        s = Slot.search().sort(SLOT_NO_DESC)
        res = s.filter("term", status=STATUS_OCCUPIED).execute()[:1]
        if res:
            return res[0].slot_no +1
        else:
            return 1


