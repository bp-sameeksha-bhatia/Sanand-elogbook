from django.shortcuts import render,redirect
from django import forms
from .models import Electrical
from .forms import ChlorinatedForm,Pcc
from accounts.models import User
from elogbook.models import Electrical
# Create your views here.
def allforms(request):
    return render(request,'electrical/all_forms.html')

def chlorinated(request):

    u1 = User.objects.get(username=request.user.username)
    user_role = u1.user_role
    print('user 1:', u1)
    print('role of user:', u1.user_role)
    c_user = None
    curr_user = None
    accept = False
    if user_role == 'SUPERVISOR':


        objs = Electrical.Chlorinated_Soft_Water_Tank.objects.all()
        users = User.objects.filter(user_role='ASSOCIATE')

        c_user = None
        curr_user_list = None

        c_user = request.GET.get('curr_user', None)
        print('rquest',request)

        if  c_user != None:

            curr_username = User.objects.get(username=c_user)
            print('curr_username',curr_username.first_name)

            curr_user_list = Electrical.Chlorinated_Soft_Water_Tank.objects.filter(done_by=curr_username.first_name)


            print('curr_user object is',curr_user_list)

        context = {'curr_user_list':curr_user_list,'objs':objs,'user_role':user_role,'users':users}
        return render(request,"electrical/chlorinated.html",context=context)
    else:
        print('inside else')
        curr_username = User.objects.get(username=request.user)
        curr_user_list = Electrical.Chlorinated_Soft_Water_Tank.objects.filter(done_by=curr_username.first_name)

        if request.method == "POST":
            print('inside post')
            form = ChlorinatedForm(request.POST)
            print('form is:',form)
            if form.is_valid():
                print('inside')
                form.save()
                print('title:',form.cleaned_data['title'])
                return redirect('/')
            else:

                data = {'done_by': request.user.first_name}
                form = ChlorinatedForm(initial=data)

                return render(request,"electrical/chlorinated.html",{'form':form,'user_role':user_role,'curr_user_list':curr_user_list})
        else:

            data = {'done_by':request.user.first_name}
            form = ChlorinatedForm(initial=data)

            print('form:',form)
            return render(request, "electrical/chlorinated.html", {'form': form,'user_role':user_role,'curr_user_list':curr_user_list})
def pcc(request):

    u1 = User.objects.get(username=request.user.username)
    user_role = u1.user_role
    print('user 1:', u1)
    print('role of user:', u1.user_role)
    if user_role == 'SUPERVISOR':
        objs = Electrical.log_sheet_pcc.objects.all()

        #print('objs:)
        return render(request,"electrical/pcc.html",{'objs':objs,'user_role':user_role})
    else:
        if request.method == "POST":
            form = Pcc(request.POST)
            #print('form is:',form)
            if form.is_valid():
                print('inside')
                form.save()
                return redirect('/')
            else:

                form = Pcc()
                return render(request,"electrical/pcc.html",{'form':form,'user_role':user_role})
        else:
            form = Pcc()
            return render(request, "electrical/pcc.html", {'form': form,'user_role':user_role})




