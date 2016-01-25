import json
import requests

from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView, View

from src.Display.Forms.parkform import ParkForm
from src.Display.helper.createurl import createurl
from src.Display.helper.removekey import removekey
from src.common.frontendconstants import *



class DashboardView(View):
    def get(self,request):
        if request.method == 'GET':
            return render_to_response(template_name = "c.html")


