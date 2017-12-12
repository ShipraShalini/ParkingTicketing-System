from src.models.model import Slot

def is_duplicate(reg_no):
    return bool(Slot.search().filter('term', registration_no=reg_no).execute())
