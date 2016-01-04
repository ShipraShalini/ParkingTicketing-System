from django.views.generic.base import TemplateView
from src.search.helper.read_request import read_request
from src.search.lib.searchclass import searchclass
from common.constants import *
from django.views.generic import View
from rest_framework import permissions
from src.search.helper.read_request import read_request
from django.http import HttpResponse
import json
from src.search.helper.helper import is_duplicate


class SearchView(View):
    def get(self, request):
        if self.request.method == 'GET':
            reg_no, colour = read_request(self.request)
            slots = searchclass.find(reg_no=reg_no, colour=colour)
            return HttpResponse(slots)













# def get_context_data(self, **kwargs):
#     if self.request.method == 'GET':
#         reg_no, colour = read_request(self.request)
#         slot = searchclass.find(reg_no=reg_no, colour=colour)
#         context = super(SearchView, self).get_context_data(**kwargs)
#         context[SLOT_INFO] = slot.__dict__
#         return context

