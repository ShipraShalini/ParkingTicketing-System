from src.backend_api.lib.assignmentlib import assignmentclass
from src.models.model import Slot
from src.common.constants import *


class AvailabilityClass(object):
    s = Slot.search().sort(SLOT_NO)

    def search_free(self):
        return self.s.filter('term', status = STATUS_FREE).execute()

    def search_occupied(self):
        return self.s.filter('term', status = STATUS_OCCUPIED).execute()

    def is_max_slot_no_reached(self):
        max_slot_no = assignmentclass.max_occupied_slot_plus_one()
        return max_slot_no or False

    def is_available(self):
        """
        to check if parking space is available
        :return: bool
        """
        is_free = self.search_free()
        return is_free or self.is_max_slot_no_reached()

    def allfree(self):
        """
        finds all the free slots
        :return: list
        """
        slots = self.search_free()
        available_slots = []
        for slot in slots:
            available_slots.append({'Slot_no': slot.slot_no})

        max_slot_no = self.is_max_slot_no_reached()
        if max_slot_no:
            for i in range(max_slot_no + 1, MAX_NO_OF_SLOTS+1):
                available_slots.append({'Slot_no': i})
        return available_slots or 'All Occupied'


availabilityclass = AvailabilityClass()
