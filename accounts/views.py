from django.shortcuts import render
from django.contrib.auth import authenticate,login
# Create your views here.

def home(request):
    context = {'user':request.user}
    print('user',context['user'])
    return render(request,'home.html',context=context)

def hr_section(request):
    return render(request,'assoc_hr_section.html',{'user':request.user.username})
def user_login(request):
    print('entered  again')
    if request.method == 'POST':
        print('inside post ')
        username = request.POST["username"]
        password = request.POST["password"]
        print('username is :',username)
        user = authenticate(username=username, password=password)
        print('user is :', user)
        if user:
            print('inside if')
            login(request,user)
            print('user is :',user)
            context = {'user':user}
            return render(request,'dashboard.html',context=context)

        else:
            return render(request,'login.html')
    else:
        return render(request, 'login.html')

def user_logout(request):
    pass