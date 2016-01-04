from src.models.model import Slot
from elasticsearch import NotFoundError

from common.constants import *


class searchclass(object):

    def regsearch(self, reg_no):
        try:
            s= Slot.search()
            slot = s.filter("term", registration_no = reg_no).execute()
        except NotFoundError:
            return False
        else:
            return slot

    def coloursearch(self, colour):
        try:
            s= Slot.search()
            slot = s.filter("term", colour = colour).execute()
        except NotFoundError:
            return False
        else:
            return slot

    def find(self, reg_no, colour):
        if reg_no:
            slot = self.regsearch(reg_no=reg_no)
        elif colour:
            slot = self.coloursearch(colour=colour)
        else:
            return False
        return slot




class Availabilityclass(object):

    def allfree(self):
        try:
            s= Slot.search()
            slot = s.filter("term", status = STATUS_FREE).execute()
        except NotFoundError:
            return False
        else:
            return slot

