from django.urls import path
from . import views
urlpatterns = [
    path('electrical/',views.allforms,name='allforms'),
    path('electrical/chlorinated/',views.chlorinated,name='electrical_chlorinated'),
    path('electrical/pcc/',views.pcc,name='electrical_pcc'),
]