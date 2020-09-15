from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar
from notification.views import global_noify_count

from .models import *
from .utils import Calendar
from .forms import EventForm

def index(request):
    return HttpResponse('hello')

class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar.html'

    def get_queryset(self):
        q = Event.objects.filter(user=self.request.user)
        return q

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('context is :',context)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        print('self is :--->',self)
        html_cal = cal.formatmonth(withyear=True,user=self.request.user)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        context['object_list'] = Event.objects.filter(user=self.request.user)
        context['notification_count'] = global_noify_count(self.request)

        #get user
        u1 = User.objects.get(username=self.request.user.username)
        user_role = u1.user_role
        context['user_role'] = user_role

        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    count = global_noify_count(request)
    print('inside event ')
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    u1 = User.objects.get(username=request.user.username)
    user_role = u1.user_role
    form=None
    if user_role == 'SUPERVISOR':
        context = {'sent_by':request.user.email}
        form = EventForm(request.POST or None, instance=instance,initial=context)

        if request.POST and form.is_valid():
            form_id = request.POST.get('form', None)
            user = request.POST.get('user', None)
            event = Event.objects.filter(form=form_id, user=user)
            if len(event)==0:
                form.save()
                return render(request, 'submitted.html', {'form': form,'user_role':user_role,'notification_count':count})
            else:
                return render(request, 'event.html',
                              {'form': form, 'user_role': user_role, 'notification_count': count})
        else:
            return render(request, 'event.html', {'form': form,'user_role':user_role,'notification_count':count})
    else:
        return render(request, 'event.html', {'form': form,'user_role':user_role,'notification_count':count})