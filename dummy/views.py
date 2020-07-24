from django.shortcuts import render
from .models import PersonForm
from .models import Person
# Create your views here.
def home_view(request):
    context = {}
    form = PersonForm
    return render(request,"index.html",{'form':form})
def my_save(request):
    form = PersonForm()
    if form.is_valid():
        data = {}
        for field in form:
            data[field] = form.cleaned_data.get(field)

        Person.save(data)
    return render(request,'success.html')
