from src.models.model import Slot
from common.constants import *



class AssignSlot():
    query ={
            "aggs" : {
                "assign_slot" : {
                    "filter" : { "term": { "status": STATUS_FREE } },

                    "aggs" : {
                        "min_slot" : { "min" : { "field" : SLOT_NO } }
                    }
                }
            }
        }


b = {'query': {'filtered': {'filter': {'term': {'status': 'Free'}}, 'query': {'match_all': {}}}}, 'aggs': {'min_slot': {'min': {'field': 'slot_no'}}}}

class AssignmentClass():

    def is_duplicate(self,reg_no):
        s = Slot.search()
        if s.filter("term", registration_no=reg_no).execute():
            return True
        else:
            return False


    def min_free_slot(self,s):
        res = s.filter("term", status=STATUS_FREE).aggs.metric("assign_slot", "min", field=SLOT_NO).execute()
        if res:
            return int(res.aggregations.assign_slot.value)
        else:
            return False



    def max_occupied_slot_plus_one(self,s):
        try:
            res = s.filter("term", status=STATUS_OCCUPIED).aggs.metric("assign_slot", "max", field=SLOT_NO).execute()
        except AttributeError:
            return 1
        else:
            if res.aggregations.assign_slot.value >= MAX_NO_OF_SLOTS :
                return False
            else:
                return int (res.aggregations.assign_slot.value + 1)

    def assign_slot(self):
        s = Slot.search()
        assigned_slot = self.min_free_slot(s)
        if assigned_slot:
            return assigned_slot
        else:
           assigned_slot = self.max_occupied_slot_plus_one(s)
           return assigned_slot

assignmentclass = AssignmentClass()

