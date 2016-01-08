import json

from django.http import HttpResponse
from django.views.generic import View
from rest_framework import permissions

from common.constants import *
from src.search.helper.read_request import read_request
from src.search.lib.actionlib import actionclass
from src.search.helper.isduplicate import is_duplicate


class ParkingView(View):
    permission_classes = (permissions.AllowAny, )
    def post(self, request):
        if request.method == 'POST':
            reg_no, colour = read_request(request)
            is_parked = is_duplicate(reg_no)
            if is_parked:
                return HttpResponse("This car is already parked")
            slot = actionclass.park(reg_no=reg_no, colour=colour)
            if slot:
                context = json.dumps(slot._d_)
                return HttpResponse(context)
            else:
                return HttpResponse(OCCUPIED_MESSAGE)
            # return render(request, 'polls/index.html', context)


    def delete(self,request):
        if request.method == 'DELETE':
            id = read_request(request)
            slot = actionclass.unpark(id =id)
            context = json.dumps(slot._d_)
            return HttpResponse(context)

            # return render(request, 'polls/index.html', context)