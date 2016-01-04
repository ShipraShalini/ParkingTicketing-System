from src.models.model import Slot
from elasticsearch import NotFoundError
from src.search.helper.helper import max_slot_no_in_DB

from common.constants import *


class SearchClass(object):

    def regsearch(self, reg_no):
        try:
            s= Slot.search()
            slot = s.filter("term", registration_no = reg_no).execute()[0]
        except NotFoundError:
            return False
        else:
            return dict(registration_no=slot.registration_no, slot_no=slot.slot_no)

    def coloursearch(self, colour):
        try:
            s= Slot.search()
            slot = s.filter("term", colour = colour).execute()
        except NotFoundError:
            return False
        else:
            slots = []
            for car in slot:
                slots.append(dict(registration_no=car.registration_no, slot_no=car.slot_no))
            return slots

    def find(self, reg_no, colour):
        if reg_no:
            slot = self.regsearch(reg_no=reg_no)
        elif colour:
            slot = self.coloursearch(colour=colour)
        else:
            return False
        return slot


searchclass = SearchClass()



class AvailabilityClass(object):
    def allfree(self):
        s= Slot.search().sort(SLOT_NO)
        slots = s.filter("term", status = STATUS_FREE).execute()

        available_slots = []
        for slot in slots:
            available_slots.append(dict(Slot_no = slot.slot_no))

        max_slot_no = max_slot_no_in_DB()
        if max_slot_no < MAX_NO_OF_SLOTS:
            for i in range(max_slot_no+1, MAX_NO_OF_SLOTS+1):
                available_slots.append(dict(Slot_no = i))

        if available_slots:
            return available_slots
        else:
            return "All Occupied"





#     def allfree(self):
#         try:
#             print "AAA"
#             s= Slot.search()
#             slot = s.filter("term", status = STATUS_FREE).execute()
#         except NotFoundError:
#             print "occupied"
#             return "All Occupied"
#         else:
#             print slot
#             slots = []
#             for car in slot:
#                 slots.append(dict(slot_no=car.slot_no))
#             return slots


availabilityclass = AvailabilityClass()

