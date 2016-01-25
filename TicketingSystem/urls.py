"""TicketingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

from src.Display.Views.dashboardview import DashboardView
from src.Display.Views.parkformview import park
from src.Display.Views.searchformview import search
from src.Display.Views.unparkformview import unpark
from src.backend_api.view.availibilityview import AvailibilityView
from src.backend_api.view.chartview import ChartView
from src.backend_api.view.parkingview import ParkingView
from src.backend_api.view.searchview import SearchView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^park/', ParkingView.as_view()),
    url(r'^search/', SearchView.as_view()),
    url(r'^available/', AvailibilityView.as_view()),
    url(r'^chart/', ChartView.as_view()),
    url(r'^search-form/', search),
    # url(r'^park-form/', ParkDisplayView.as_view()),
    url(r'^park-form/', park),
    url(r'^unpark-form/', unpark),
    url(r'^dashboard/', DashboardView.as_view()),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
