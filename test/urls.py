from django.urls import path, re_path
from .views import *

form = Form()

urlpatterns = [
    path("index", show_form_list,name='allforms'),
    path("supervisor_form",supervisor_form,name='supervisor_form'),
    path("form",create_form,name='form_cur_user'),
    path("form/<int:pk>/", create_form, name='form'),
    path("submitted", save_form, name='form_submit')
]
