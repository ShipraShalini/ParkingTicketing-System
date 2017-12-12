
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
from rest_framework import permissions
from rest_framework.generics import GenericAPIView

from src.backend_api.helper.countpercolour import count_per_colour


class ChartView(GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    def get(self,request):
        if request.method == 'GET':
            data = json.dumps(count_per_colour())
            return HttpResponse(content=data, content_type="application/json")
