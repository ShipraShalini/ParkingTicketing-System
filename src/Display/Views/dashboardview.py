from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView, View


class DashboardView(View):
    def get(self,request):
        if request.method == 'GET':
            return render_to_response(template_name = 'c.html')
