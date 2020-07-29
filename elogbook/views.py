from django.shortcuts import render,redirect
from django import forms
from .models import Electrical
from .forms import ChlorinatedForm
from accounts.models import User
from elogbook.models import Electrical
# Create your views here.
def chlorinated(request):

    u1 = User.objects.get(username=request.user.username)
    user_role = u1.user_role
    print('user 1:', u1)
    print('role of user:', u1.user_role)
    if user_role == 'SUPERVISOR':
        objs = Electrical.Chlorinated_Soft_Water_Tank.objects.all()

        #print('objs:)
        return render(request,"electrical/chlorinated.html",{'objs':objs,'user_role':user_role})
    else:
        if request.method == "POST":
            form = ChlorinatedForm(request.POST)
            #print('form is:',form)
            if form.is_valid():
                print('inside')
                form.save()
                print('title:',form.cleaned_data['title'])
                return redirect('/')
            else:

                form = ChlorinatedForm()
                return render(request,"electrical/chlorinated.html",{'form':form,'user_role':user_role})
        else:
            form = ChlorinatedForm()
            return render(request, "electrical/chlorinated.html", {'form': form,'user_role':user_role})


