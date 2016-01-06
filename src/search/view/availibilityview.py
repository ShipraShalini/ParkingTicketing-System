from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views.generic import View
from src.search.lib.availibilitylib import availabilityclass


# class SearchView(View):
#     def get(self, request):
#         if self.request.method == 'GET':
#             reg_no, colour = read_request(self.request)
#             slots = searchclass.find(reg_no=reg_no, colour=colour)
#             return HttpResponse(slots)


class AvailibilityView(View):
    def get(self,request):
        if self.request.method == 'GET':
            slot = availabilityclass.allfree()
            print "Slot:", slot
            return HttpResponse(slot)
