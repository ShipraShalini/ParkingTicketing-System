from django.http import HttpResponse
from django.views.generic import View

from src.backend_api.lib.availibilitylib import availabilityclass


class AvailibilityView(View):

    def get(self, request):
        if request.method == 'GET':
            slot = availabilityclass.allfree()
            return HttpResponse(slot)
