
'''
print "Content-Type: text/html\n"
print """<html><body>
...a bunch of text and html here...
<img src="data:image/png;base64,%s"/>
...more text and html...
</body></html>""" % sio.getvalue().encode("base64").strip()
'''
from django.http import HttpResponse
from django.views.generic import View

from src.backend_api.helper.countpercolour import count_per_colour
from src.backend_api.lib.availibilitylib import availabilityclass
from src.backend_api.lib.barchartlib import barchart
from src.backend_api.lib.piechartlib import piechart


class ChartView(View):

    def get(self, request):
        if request.method == 'GET':

            data = count_per_colour()
            bc = barchart.drawchart(data)

            no_of_occupied_slots = availabilityclass.search_occupied().hits.total
            pc = piechart.drawchart(no_of_occupied_slots)



            return HttpResponse(HTML_CODE.format(bc, bc))



