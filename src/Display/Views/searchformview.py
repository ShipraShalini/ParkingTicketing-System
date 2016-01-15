from django.http import HttpResponse
from django.shortcuts import render

from src.Display.Forms.searchform import SearchForm
from src.Display.helper.createurl import createurl
from src.Display.helper.removekey import removekey
from src.common.frontendconstants import *

import requests, json


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            url=createurl(SEARCHURL)
            print url
            print form.cleaned_data, type(form.cleaned_data)
            params = dict((k, v) for k, v in form.cleaned_data.iteritems() if v)
            print "Non-Empty", params
            # response = requests.get(url=url,params=params)._content
            response = json.loads(requests.get(url=url, params=params)._content)
            # print "Response", response, type(response)
            context= dict(data=response)
            # print context , type(context)
            return render(request, 'park.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, 'form.html', {'link': 'search-form', 'form': form})