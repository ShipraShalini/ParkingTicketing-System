import json

import requests

from django.shortcuts import render

from src.Display.Forms.parkform import ParkForm
from src.Display.helper.createurl import createurl
from src.Display.helper.removekey import removekey
from src.common.frontendconstants import *


def park (request):
    if request.method == 'POST':
        form = ParkForm(request.POST)
        if form.is_valid():
            url=createurl(PARKURL)
            response = json.loads(
                requests.post(
                    url=url,
                    data=json.dumps(form.cleaned_data)
                )._content
            )
            removekey(response, 'status')
            context = {'data': response}
            return render(request, 'park.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ParkForm()

    return render(request, 'form.html', {'link': 'park-form', 'form': form})
