from django.shortcuts import render,redirect
from .models import Schedule
from accounts.models import User
from .forms import CalendarForm
# Create your views here.
def schedule(request):
    u1 = User.objects.get(username=request.user.username)
    user_role = u1.user_role
    if user_role == 'SUPERVISOR':
        if request.method == 'POST':
            form = CalendarForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
            else:
                form = CalendarForm(initial={'sent_by':request.user})
                context = {

                    'user_role': user_role,
                    'form': form,
                }
                return render(request,"sanand_calendar/calendar.html",context=context)
        else:
            form = CalendarForm(initial={'sent_by': request.user})
            context = {

                'user_role': user_role,
                'form': form,
            }
            return render(request, "sanand_calendar/calendar.html", context=context)

    else:
        cal = Schedule.objects.all()
        sch = None
        if user_role == 'ASSOCIATE':
            sch = Schedule.objects.filter(user=request.user)[:]
            print('sch:',sch)


        context = {'sent_by':request.user}
        form = CalendarForm(initial=context)
        #form.fields['user'].query_set = User.objects.filter(user_role='ASSOCIATE')
        print('users....',User.objects.filter(user_role='ASSOCIATE'))
        context = {
            'cal':cal,
            'user_role':user_role,
            'form':form,
            'sch':sch,
        }
        return render(request,"sanand_calendar/calendar.html",context=context)
