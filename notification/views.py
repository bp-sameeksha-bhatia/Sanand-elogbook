from django.shortcuts import render,redirect
from djangocalendar.models import Event
from test.models import Data
from django.db.models import Q
# Create your views here.
def global_noify_count(request):
    count = 0
    if request.user.user_role =='ASSOCIATE':
        #events = Event.objects.filter(user=request.user,status='SEND_BACK')
        count = Event.get_associate_notification(request.user)
    elif request.user.user_role == 'SUPERVISOR':
        #events = Event.objects.filter(user__dept=request.user.dept,status='SEND_BACK')
        count = Event.get_supervisor_notification(sent_by=request.user.email)
    return count

def notify(request):
    count=0
    events=None
    if request.user.user_role == 'ASSOCIATE':
        events = Event.objects.filter(status__in = ['INITIAL','Send Back','Form Sent'],user=request.user).order_by('modified')
        print('events :',events)
        count = global_noify_count(request)
        print('count is ',count)

    elif request.user.user_role == 'SUPERVISOR':
        events = Event.objects.filter(status__in=['Send Back','Form Sent'],user__dept=request.user.dept).order_by('modified')
        count = global_noify_count(request)
        print('count is ', count)
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







