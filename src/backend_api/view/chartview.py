
'''
print "Content-Type: text/html\n"
print """<html><body>
...a bunch of text and html here...
<img src="data:image/png;base64,%s"/>
...more text and html...
</body></html>""" % sio.getvalue().encode("base64").strip()
'''
import json

from django.http import HttpResponse
from django.views.generic import View
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from src.backend_api.helper.countpercolour import count_per_colour
from src.backend_api.lib.availibilitylib import availabilityclass
from src.backend_api.lib.barchartlib import barchart
from src.backend_api.lib.piechartlib import piechart


class ChartView(GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    def get(self,request):
        if self.request.method == 'GET':
            data = json.dumps(count_per_colour())
            return HttpResponse(content=data, content_type="application/json")


