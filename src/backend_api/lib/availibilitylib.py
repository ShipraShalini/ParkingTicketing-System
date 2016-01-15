from src.backend_api.lib.assignmentlib import assignmentclass
from src.models.model import Slot
from src.common.constants import *

class AvailabilityClass(object):
    s= Slot.search().sort(SLOT_NO)

    def search_free(self):
        slots = self.s.filter("term", status = STATUS_FREE).execute()
        return slots

    def search_occupied(self):
        slots = self.s.filter("term", status = STATUS_OCCUPIED).execute()
        return slots

    def is_max_slot_no_reached(self):
        max_slot_no = assignmentclass.max_occupied_slot_plus_one()
        if max_slot_no:
            return max_slot_no
        else:
            return False

    def is_available(self):
        '''
        to check if parking space is available
        :return: bool
        '''
        is_free = self.search_free()
        if is_free:
            return is_free
        elif self.is_max_slot_no_reached():
            return True
        else:
            return False


    def allfree(self):
        '''
        finds all the free slots
        :return: list
        '''
        slots = self.search_free()
        available_slots = []
        for slot in slots:
            available_slots.append(dict(Slot_no = slot.slot_no))
        print "A", available_slots

        max_slot_no = self.is_max_slot_no_reached()
        if max_slot_no:
            for i in range(max_slot_no+1, MAX_NO_OF_SLOTS+1):
                available_slots.append(dict(Slot_no = i))
            print "B", available_slots

        if available_slots:
            return available_slots
        else:
            return "All Occupied"


availabilityclass = AvailabilityClass()