from django.http import HttpResponse
from django.views.generic import View
from rest_framework import permissions

from src.backend_api.helper.isduplicate import is_duplicate
from src.backend_api.helper.read_request import read_request
from src.backend_api.helper.createmessagestring import createmessagestring
from src.backend_api.lib.actionlib import actionclass
from src.common.constants import *

import json


class ParkingView(View):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        if request.method == 'POST':
            reg_no, colour = read_request(request)
            print "BACK:", reg_no, colour
            is_parked = is_duplicate(reg_no)
            if is_parked:
                message = createmessagestring(ALREADY_PARKED_MESSAGE)
                return HttpResponse(message,  content_type="application/json")
            slot = actionclass.park(reg_no=reg_no, colour=colour)
            if slot:
                context = json.dumps(slot._d_)
                return HttpResponse(context)
            else:
                message = createmessagestring(OCCUPIED_MESSAGE)
                return HttpResponse(message, content_type="application/json")
            # return render(request, 'polls/index.html', context)

    def delete(self,request):
        if request.method == 'DELETE':
            id = read_request(request)
            slot = actionclass.unpark(id =id)
            context = json.dumps(slot._d_)
            return HttpResponse(context,  content_type="application/json")
