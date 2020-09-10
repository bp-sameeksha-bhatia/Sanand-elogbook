from django.shortcuts import render,redirect
from djangocalendar.models import Event
from test.models import Data
from django.db.models import Q
# Create your views here.
def global_noify_count(request):
    if request.user.user_role =='ASSOCIATE':
        events = Event.objects.filter(user=request.user)
        count = Event.get_associate_notification(request.user)
    elif request.user.user_role == 'SUPERVISOR':
        events = Event.objects.filter(user__dept=request.user.dept)
        count = Event.get_supervisor_notification(sent_by=request.user.email)
    return count

def notify(request):
    count=0
    events=None
    if request.user.user_role == 'ASSOCIATE':
        events = Event.objects.filter(user=request.user).order_by('-id')
        count = global_noify_count(request)

    elif request.user.user_role == 'SUPERVISOR':
        events = Event.objects.filter(user__dept=request.user.dept).order_by('-id')
        count = global_noify_count(request)
    return render(request,'notification.html',context={'notification_count':count,'events':events,'user_role':request.user.user_role})

def unread(request,event_id):
    event = Event.objects.get(id=event_id)
    if request.user.user_role == 'ASSOCIATE':
        event.read_unread = True
        event.save()
    elif request.user.user_role == 'SUPERVISOR':
        event.supervisor_read = True
        event.save()

    return redirect('notify')







