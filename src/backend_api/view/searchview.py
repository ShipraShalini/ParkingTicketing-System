import json

from django.http import HttpResponse
from django.views.generic import View

from src.backend_api.helper.read_request import read_request
from src.backend_api.lib.searchlib import searchclass


class SearchView(View):
    def get(self, request):
        if self.request.method == 'GET':
            reg_no, colour = read_request(self.request)
            slots = searchclass.find(reg_no=reg_no, colour=colour)
            slots = json.dumps(slots)
            return HttpResponse(slots, content_type="application/json")
