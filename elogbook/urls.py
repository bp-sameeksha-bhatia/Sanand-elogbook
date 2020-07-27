from django.urls import path
from . import views
urlpatterns = [
    path('electrical/chlorinated/',views.chlorinated,name='electrical_chlorinated'),
]