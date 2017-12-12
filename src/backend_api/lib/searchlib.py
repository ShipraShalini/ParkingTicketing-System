from elasticsearch import NotFoundError

from src.models.model import Slot


class SearchClass(object):

    def regsearch(self, reg_no):
        try:
            s = Slot.search()
            slot = s.filter("term", registration_no = reg_no).execute()[0]
        except NotFoundError:
            return False
        else:
            return {
                'registration_no': slot.registration_no,
                'slot_no': slot.slot_no,
                'colour': slot.colour
            }

    def coloursearch(self, colour):
        try:
            s = Slot.search()
            slot = s.filter("term", colour = colour).execute()
        except NotFoundError:
            return False
        else:
            slots = []
            for car in slot:
                slots.append({
                    'registration_no': car.registration_no,
                    'slot_no': car.slot_no,
                })
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
