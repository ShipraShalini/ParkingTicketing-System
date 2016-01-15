from src.models.model import Slot

def is_duplicate(reg_no):
        s = Slot.search()
        if s.filter("term", registration_no=reg_no).execute():
            return True
        else:
            return False