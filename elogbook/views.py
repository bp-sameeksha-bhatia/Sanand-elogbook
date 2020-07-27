from django.shortcuts import render,redirect
from django import forms
from .models import Electrical
from .forms import ChlorinatedForm
# Create your views here.
def chlorinated(request):
    print('inside view')
    if request.method == "POST":
        form = ChlorinatedForm(request.POST)
        print('form is:',form)
        if form.is_valid():
            print('inside')
            form.save()
            print('title:',form.cleaned_data['title'])
            return redirect('/')
        else:

            form = ChlorinatedForm()
            return render(request,"electrical/chlorinated.html",{'form':form})
    else:
        form = ChlorinatedForm()
        return render(request, "electrical/chlorinated.html", {'form': form})


