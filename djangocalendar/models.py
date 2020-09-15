from django.db import models
from django.urls import reverse
from django.shortcuts import render
from test.models import Form
from accounts.models import User
from accounts.models import AbstractAccessInfoModel

from django.db.models import Q

# Create your models here.
class Event(AbstractAccessInfoModel):
    choice = (
        ('ACCEPTED', 'Accepted'),
        ('REJECTED', 'Reject'),
        ('SEND_BACK', 'Send_Back'),
        ('Form_Sent', 'Form_Sent'),
        ('INITIAL','Initial'),

    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    form = models.ForeignKey(Form, on_delete=models.CASCADE,blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_role': 'ASSOCIATE'},blank=True,null=True)
    status = models.CharField(max_length=512, choices=choice, default='INITIAL')
    form_remarks = models.TextField(max_length=1000, default='No Remarks')
    sent_by = models.CharField(max_length=300)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    read_unread = models.BooleanField(default=False)
    supervisor_read = models.BooleanField(default=False)

    @property
    def get_html_url(self):
        url = reverse('form', args=(self.form.id,self.id))
        return f'<a href="{url}"> {self.form} </a>'

    @property
    def get_form_url(self):
        url = reverse('form', args=(self.form.id, self.id))
        return url

    @property
    def get_form_id(self):
        return self.form.id

    @staticmethod
    def get_associate_notification(user):
        event_unread = Event.objects.filter(status__in = ['INITIAL','Send Back','Form Sent'],user=user,read_unread=False,)
        unread = len(event_unread)
        return unread

    @staticmethod
    def get_supervisor_notification(sent_by):
        event_unread = Event.objects.filter(status__in=['Send Back','Form Sent'],sent_by=sent_by, supervisor_read=False)
        unread = len(event_unread)
        return unread


