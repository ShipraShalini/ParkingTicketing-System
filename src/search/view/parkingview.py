from django.views.generic.base import TemplateView
from django.views.generic import View
from rest_framework import permissions
from rest_framework.views import APIView
from src.search.helper.read_request import read_request
from src.search.lib.actionclass import actionclass
from django.shortcuts import render
from common.constants import *
from rest_framework.response import Response
from django.http import HttpResponse
import json

# class ParkingView(TemplateView):
#
#     def get_context_data(self, **kwargs):
#         if self.request.method == 'POST':
#             reg_no, colour = read_request.post(self.request)
#             slot = actionclass.park(reg_no=reg_no, colour=colour)
#         if self.request.method == 'DELETE':
#             reg_no, colour = read_request.post(self.request)
#             slot = actionclass.unpark(id =id)
#         context = super(ParkingView, self).get_context_data(**kwargs)
#         context[SLOT_INFO] = slot.__dict__
#         return context

class ParkingView(View):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        if request.method == 'POST':
            reg_no, colour = read_request(request)
            slot = actionclass.park(reg_no=reg_no, colour=colour)
            context = json.dumps(slot._d_)
            return HttpResponse(context)
            # return render(request, 'polls/index.html', context)


    def delete(self,request):
        if request.method == 'DELETE':
            id = read_request(request)
            slot = actionclass.unpark(id =id)
            context = json.dumps(slot._d_)
            return HttpResponse(context)

            # return render(request, 'polls/index.html', context)