import json

from django.shortcuts import render
from .models import *
from accounts.models import User
from django.db.models import Q
from djangocalendar.models import Event
from notification.views import global_noify_count
from notification.views import notify
from django.http import  HttpResponse
from .resources import DataResource
import json
import csv

def export(request,queryset):
    data_resource = DataResource()
    dataset = data_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="form_data.csv"'
    writer = csv.writer(response)
    count = 0
    # print(json.dumps(queryset[0].details))
    for obj in queryset:
        # loop through all the fields in the current post object
        for field in obj._meta.fields:
            # find the fields with JSONField type
            if obj._meta.get_field(field.name).get_internal_type() == 'JSONField':
                # get the contents of the json field and convert it into json format
                detail = json.dumps(getattr(obj, field.name))
                # detail = "'" + detail + "'"
                detail_parsed = json.loads(str(detail))
                # lists to store the keys and values from the json
                keys = []
                values = []
                # loop through each json row and make a list of the keys and values
                for key, value in detail_parsed.items():
                    keys.append(key)
                    values.append(value)
                # write the values into csv file
                # keys form the column headers so write them only once
                if count == 0:
                    writer.writerow(keys)
                    count += 1
                # write the values in each row
                writer.writerow(values)
    return response
def export_json_field(modeladmin, request, queryset):
    '''
    Exports the JSON fields in a model to csv file
    '''
    #Create the httpResponse object with correct csv header
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Json2Csv.csv"'
    writer = csv.writer(response)
    count = 0
    # print(json.dumps(queryset[0].details))
    for obj in queryset:
        #loop through all the fields in the current post object
        for field in obj._meta.fields:
            #find the fields with JSONField type
            if obj._meta.get_field(field.name).get_internal_type() == 'JSONField':
                #get the contents of the json field and convert it into json format
                detail = json.dumps(getattr(obj,field.name))
                #detail = "'" + detail + "'"
                detail_parsed = json.loads(str(detail))
                #lists to store the keys and values from the json
                keys = []
                values = []
                #loop through each json row and make a list of the keys and values
                for key, value in detail_parsed.items():
                    keys.append(key)
                    values.append(value)
                # write the values into csv file
                # keys form the column headers so write them only once
                if count == 0:
                    writer.writerow(keys)
                    count += 1
                # write the values in each row
                writer.writerow(values)
    return response
export_json_field.short_description = 'Export Json TO Csv'


def show_form_list(request):
    all_events = Event.objects.filter(sent_by=request.user.email)
    all_forms = []
    for a_event in all_events:
        all_forms.append([a_event.form.id,a_event.id,a_event.form])
    return render(request, "test_index.html", {"all_forms": all_forms,'notification_count':global_noify_count(request)})

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



def create_form(request,pk,event_id):
    form_id=request.POST.get('form_id')
    data_form_pk = request.POST.get('dataformpk')
    if 'reject' in request.POST:
        data = Event.objects.get(form=data_form_pk)
        data.status = 'Reject'
        data.form_remarks = request.POST.get('extracomments')
        data.save()

    elif 'accept' in request.POST:
        data = Event.objects.get(form=data_form_pk)
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
        data = Event.objects.get(form=data_form_pk)
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
            data = []
            event = Event.objects.filter(~Q(status='ACCEPTED'),user=c_user,form=form)
            data = Data.objects.filter(event__in=event)

            curr_form_data = []
            print('form data is ----', data)
            for d in data:
                if d.event.status!="Accepted":
                    curr_form_data.append([d.event.form.id,d.form_data,d.event.id,d.event])
            print('form data is ----',curr_form_data)
            #for index,d in enumerate(data):



            '''
            for index,d in enumerate(data):
                print('d: status :---->',d.status)
                if d.user == c_user and d.form==form and d.status!='Accepted':
                    #d.form_data['form_status'] = [d.status]
                    curr_form_data.append([d.form,datas])
            '''

    all_forms = Form.objects.all()


    all_form_fields = form.field.all()
    all_form_options = []
    for a_field in all_form_fields:
        all_form_options.append(a_field.options.all())
    print('all_form_fields --->',all_form_options)


    u1 = User.objects.get(username=request.user.username)
    user_role = u1.user_role

    users = User.objects.filter(user_role='ASSOCIATE')

    #print('curr_user_form',curr_form_data)
    context = {"all_form_fields": form.field, "all_form_options": all_form_fields,
               'user_role':user_role,'all_forms':all_forms,'users':users,
               'curr_user':c_user,'curr_user_forms':curr_form_data,'form_id':form.id,'event_id':event_id,'notification_count':global_noify_count(request)}
    return render(request, "test_form.html",context=context)


def save_form(request):
    data = Data()
    event = Event.objects.get(id=request.POST.get('event_id'))
    print('request.post',request.POST)
    data.event = event
    print('request is : --',request)
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
    context = {'notification_count':global_noify_count(request)}
    return render(request, "submitted.html",context=context)
