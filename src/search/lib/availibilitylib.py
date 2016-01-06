from common.constants import SLOT_NO, STATUS_FREE, MAX_NO_OF_SLOTS
from src.models.model import Slot
from src.search.helper.helper import max_slot_no_in_DB


class AvailabilityClass(object):

    def search_free(self):
        s= Slot.search().sort(SLOT_NO)
        slots = s.filter("term", status = STATUS_FREE).execute()
        return slots

    def is_max_slot_no_reached(self):
        max_slot_no = max_slot_no_in_DB()
        if max_slot_no < MAX_NO_OF_SLOTS:
            return max_slot_no
        else:
            return False

    def is_available(self):
        is_free = self.search_free()
        if is_free:
            return is_free
        elif self.is_max_slot_no_reached():
            return True
        else:
            return False


    def allfree(self):
        slots = self.search_free()

        available_slots = []
        for slot in slots:
            available_slots.append(dict(Slot_no = slot.slot_no))

        max_slot_no = self.is_max_slot_no_reached()
        if max_slot_no:
            for i in range(max_slot_no+1, MAX_NO_OF_SLOTS+1):
                available_slots.append(dict(Slot_no = i))

        if available_slots:
            return available_slots
        else:
            return "All Occupied"


availabilityclass = AvailabilityClass()