from pylab import *
from common.constants import *

class piechart():
    def fraction(self,part):
        occupied = 100 * float(part)/float(MAX_NO_OF_SLOTS)
        free = 100 - occupied
        return [occupied, free]

    def drawchart(self, occupied):
        labels = [LABEL_OCCUPIED, LABEL_FREE]
        fracs =self.fraction(occupied)
        explode=(0, 0.05)
        pie(fracs, explode=explode, labels=labels,
                        autopct='%1.1f%%', shadow=True, startangle=90)

        title(LABEL_STATUS_TITLE, bbox={'facecolor':'0.8', 'pad':5})
        show()