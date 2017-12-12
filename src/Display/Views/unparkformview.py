import json

import requests

from django.shortcuts import render

from src.Display.Forms.unparkform import UnparkForm
from src.Display.helper.createurl import createurl
from src.common.frontendconstants import *


def unpark(request):
    if request.method == 'GET':
        form = UnparkForm(request.POST)
        if form.is_valid():
            url = createurl(UNPARKURL)
            id = form.cleaned_data['id']
            response = json.loads(requests.delete(url=url, params=id)._content)
            context = {'data': response}
            return render(request, 'park.html', context)
    else:
        form = UnparkForm()

    return render(request, 'form.html', {'link': 'unpark-form', 'form': form})
