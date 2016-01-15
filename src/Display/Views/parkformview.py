from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import render
import requests, json

from src.Display.Forms.parkform import ParkForm
from src.Display.helper.createurl import createurl
from src.Display.helper.removekey import removekey
from src.common.frontendconstants import *


# class ParkDisplayView(TemplateView):
#     template_name = VIDEOINFOHTML
#
#     def get_context_data(self,**kwargs):
#         if self.request.method == 'GET':
#             id = self.request.GET.get('id', None)
#             url = createurl(type=VIDEO, id=id)
#             response = json.loads(requests.get(url)._content)
#             context = super(VideoInfoView, self).get_context_data(**kwargs)
#             context[VIDEOINFO] = response
#             return context
#
# class ParkDisplayView(TemplateView):
#     template_name = 'park.html'
#
#     def get_context_data(self,**kwargs):
#         if self.request.method == 'POST':
#             form = ParkForm(self.request.POST)
#             if form.is_valid():
#                 url=createurl(PARKURL)
#                 response = json.loads(requests.post(url=url, data=json.dumps(form.cleaned_data))._content)
#                 removekey(response, 'status')
#                 context = super(ParkDisplayView, self).get_context_data(**kwargs)
#                 context['park_data'] = response
#                 return context
#         else:
#             form = ParkForm()
#         return render(self.request, 'form.html', {'link': 'park-form', 'form': form})




def park (request):
    if request.method == 'POST':
        form = ParkForm(request.POST)
        if form.is_valid():
            url=createurl(PARKURL)
            # print url
            # print form.cleaned_data
            response = json.loads(requests.post(url=url, data=json.dumps(form.cleaned_data))._content)
            removekey(response, 'status')
            context= dict(data=response)
            return render(request, 'park.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ParkForm()

    return render(request, 'form.html', {'link': 'park-form', 'form': form})