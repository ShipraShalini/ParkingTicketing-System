
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
from src.backend_api.helper.create_html import barchart


class TestChartView(View):

    def get(self, request):
        if request.method == 'GET':
            data = count_per_colour()
            res = barchart.drawchart(data)

            return HttpResponse(res)
