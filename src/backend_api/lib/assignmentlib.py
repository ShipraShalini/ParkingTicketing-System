from src.models.model import Slot
from src.common.constants import *


class AssignmentClass(object):
    s = Slot.search()

    def min_free_slot(self):
        res = self.s.filter(
            'term',
            status=STATUS_FREE
        ).aggs.metric(
            'assign_slot',
            'min',
            field=SLOT_NO
        ).execute()
        if res:
            return int(res.aggregations.assign_slot.value)
        else:
            return False

    def max_occupied_slot_plus_one(self):
        try:
            res = self.s.filter(
                'term',
                status=STATUS_OCCUPIED
            ).aggs.metric(
                'assign_slot',
                'max',
                field=SLOT_NO
            ).execute()
        except AttributeError:
            return 1
        else:
            if res.aggregations.assign_slot.value >= MAX_NO_OF_SLOTS :
                return False
            else:
                return int(res.aggregations.assign_slot.value + 1)

    def assign_slot(self):
        assigned_slot = self.min_free_slot()
        return assigned_slot or self.max_occupied_slot_plus_one()


assignmentclass = AssignmentClass()
