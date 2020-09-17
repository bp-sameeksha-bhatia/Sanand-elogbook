from django.conf.urls import url
from django.urls import path
from djangocalendar import views

app_name = 'cal'
urlpatterns = [
    path('event/new/',views.event, name='event_new'),
    url('', views.CalendarView.as_view(), name='calendar_schedule'),
	url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
    url(r'^index/$', views.index, name='index'),

]