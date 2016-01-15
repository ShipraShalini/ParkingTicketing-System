from django.http import HttpResponse
from django.shortcuts import render

from src.Display.Forms.unparkform import UnparkForm
from src.Display.helper.createurl import createurl
from src.common.frontendconstants import *

import requests, json


def unpark(request):
    if request.method == 'GET':
        form = UnparkForm(request.POST)
        if form.is_valid():
            url=createurl(UNPARKURL)
            print url
            print form.cleaned_data, type(form.cleaned_data)
            id = form.cleaned_data['id']
            response = json.loads(requests.delete(url=url, params=id)._content)
            print "Response", response, type(response)
            context= dict(data=response)
            # print context , type(context)
            return render(request, 'park.html', context)
    else:
        form = UnparkForm()

    return render(request, 'form.html', {'link': 'unpark-form', 'form': form})