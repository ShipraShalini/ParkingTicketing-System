from src.models.model import Slot
from common.constants import *
from src.search.helper.helper import assignmentclass

class ActionClass(object):

    def park(self, reg_no, colour ):
        id = assignmentclass.assign_slot()
        if not id:
            return False
        slot = Slot.get(id =id, ignore=404)
        if not slot:
            slot = Slot(meta={'id': id})
            slot.slot_no = id
        slot.status = STATUS_OCCUPIED
        slot.colour = colour
        slot.registration_no = reg_no
        slot.save()
        return slot

    def unpark(self,id):
        slot = Slot.get(id =id)
        slot.status = STATUS_FREE
        slot.colour = BLANK
        slot.registration_no = BLANK
        slot.save()
        return slot


actionclass = ActionClass()




