import json

import requests

from django.shortcuts import render

from src.Display.Forms.searchform import SearchForm
from src.Display.helper.createurl import createurl
from src.common.frontendconstants import *


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            url = createurl(SEARCHURL)
            params = {(k, v) for k, v in form.cleaned_data.iteritems() if v}
            response = json.loads(requests.get(url=url, params=params)._content)
            context= {'data': response}
            return render(request, 'park.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, 'form.html', {'link': 'search-form', 'form': form})
