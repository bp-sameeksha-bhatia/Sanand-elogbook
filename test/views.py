import json

from django.shortcuts import render
from .models import *
from accounts.models import User
from django.db.models import Q

def show_form_list(self):
    all_forms = Form.objects.all()
    return render(self, "test_index.html", {"all_forms": all_forms})

def supervisor_form(request):
    form_id = request.POST.get('form_id')

    if 'extracomments' in request.POST:
        data_form_pk = request.POST['extracommentsid']
        print('form _pk is:', data_form_pk)
        data = Data.objects.get(pk=data_form_pk)
        data.form_remarks = request.POST['extracomments']
        print('extra comments are ****:',request.POST['extracomments'])
        data.save()

    curr_user = None
    cu = None
    c_user = None
    cu = request.GET.get('curr_user', None)
    curr_form_data = []
    form = Form.objects.get(id=form_id)

    if cu != None:
        c_user = User.objects.get(username=cu)
        if c_user:
            data = Data.objects.filter(~Q(status='ACCEPTED'))
            for index, d in enumerate(data):
                print('d: status :---->', d.status)
                if d.user == c_user and d.form == form and d.status != 'Accepted':
                    d.form_data['form_status'] = [d.status]
                    curr_form_data.append([d.pk, d.form_data])

    all_forms = Form.objects.all()

    all_form_fields = form.field.all()
    all_form_options = Options.objects.filter(field__in=all_form_fields)
    u1 = User.objects.get(username=request.user.username)
    user_role = u1.user_role

    users = User.objects.filter(user_role='ASSOCIATE')

    # print('curr_user_form',curr_form_data)
    context = {"all_form_fields": form.field, "all_form_options": all_form_options,
               'user_role': user_role, 'all_forms': all_forms, 'users': users,
               'curr_user': c_user, 'curr_user_forms': curr_form_data, 'form_id': form.id}
    return render(request, "test_form.html", context=context)



def create_form(request,pk):
    form_id=request.POST.get('form_id')
    data_form_pk = request.POST.get('dataformpk')
    if 'reject' in request.POST:
        print('rejected')
        print('form _pk is:', data_form_pk)
        data = Data.objects.get(pk=data_form_pk)
        data.status = 'Reject'
        data.form_remarks = request.POST.get('extracomments')
        data.save()

    elif 'accept' in request.POST:
        print('accepted')
        print('form _pk is:',data_form_pk)
        data = Data.objects.get(pk=data_form_pk)
        print('data is :',data)
        data.status = 'Accepted'
        data.form_remarks = request.POST.get('extracomments')
        data.save()

        '''
        if 'extracomments' in request.POST:
            print('extra comments are there')
            data.form_remarks = request.POST.get('extracomments')
            print('extra comments are ****:', request.POST.get('extracomments'))
            data.save()
        '''
    elif 'send_back' in request.POST:
        print('send back ')

        print('form _pk is:', data_form_pk)
        data = Data.objects.get(pk=data_form_pk)
        data.status = 'Send Back'
        data.form_remarks = request.POST.get('extracomments')
        data.save()
    '''
    elif 'extracomments' in request.POST:
        print('extra comments are there')
        data = Data.objects.get(pk=data_form_pk)
        data.form_remarks = request.POST.get('extracomments')
        print('extra comments are ****:', request.POST.get('extracomments'))
        data.save()
    '''

    curr_user = None
    cu=None
    c_user=None
    cu = request.GET.get('curr_user', None)
    curr_form_data = []
    form = Form.objects.get(id=pk)

    if cu != None:
        c_user = User.objects.get(username=cu)
        if c_user:
            data = Data.objects.filter(~Q(status='ACCEPTED'))
            for index,d in enumerate(data):
                print('d: status :---->',d.status)
                if d.user == c_user and d.form==form and d.status!='Accepted':
                    d.form_data['form_status'] = [d.status]
                    curr_form_data.append([d.pk, d.form_data])


    all_forms = Form.objects.all()


    all_form_fields = form.field.all()
    all_form_options = Options.objects.filter(field__in=all_form_fields)
    u1 = User.objects.get(username=request.user.username)
    user_role = u1.user_role

    users = User.objects.filter(user_role='ASSOCIATE')

    #print('curr_user_form',curr_form_data)
    context = {"all_form_fields": form.field, "all_form_options": all_form_options,
               'user_role':user_role,'all_forms':all_forms,'users':users,
               'curr_user':c_user,'curr_user_forms':curr_form_data,'form_id':form.id}
    return render(request, "test_form.html",context=context)


def save_form(request):
    data = Data()
    data.form = Form.objects.get(id=request.POST.get('form_id'))
    data.user = User.objects.get(id=request.user.id)
    all_form_fields = Form.objects.get(id=request.POST.get('form_id')).field.all()
    all_form_options = Options.objects.filter(field__in=all_form_fields)
    json_data = {}
    for a_field in all_form_fields:
        if a_field.type == "CHOICE+REMARK":
            li = []
            #print(type(request.POST.get(a_field.field_name+"_text")))
            #print(type(request.POST.get(a_field.field_name+"_radio")))
            if len(request.POST.get(a_field.field_name+"_text"))>1:
                li.append(request.POST.get(a_field.field_name+"_text"))
            if request.POST.get(a_field.field_name+"_radio") is not None:
                li.append(request.POST.get(a_field.field_name+"_radio"))
            json_data[a_field.field_name] = li
        else:
            json_data[a_field.field_name] = [request.POST.get(a_field.field_name)]

    data.form_data = json_data
    data.save()
    return render(request, "submitted.html")
