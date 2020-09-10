from django.contrib import admin
from django.urls import path,re_path
from django.urls import include
from django.views.generic import TemplateView
import accounts
from . import views
from notification import views

urlpatterns = [
    path('',views.notify,name='notify'),
    path('unread/<int:event_id>',views.unread,name='unread_notification'),
]