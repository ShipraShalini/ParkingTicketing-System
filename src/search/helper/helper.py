from src.models.model import Slot
from common.constants import *


def is_duplicate(reg_no):
    s = Slot.search()

    if s.filter("term", registration_no=reg_no).execute():
        return True
    else:
        return False


def max_slot_no_in_DB():
    s = Slot.search().sort(SLOT_NO_DESC)
    res = s.query("match_all").execute()[:1]
    if res:
            return res[0].slot_no
    else:
            return 0


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


