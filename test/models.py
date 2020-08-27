from django.db import models
from django.shortcuts import render
from django.contrib.postgres.fields import JSONField
from accounts.models import AbstractAccessInfoModel, User
from nested_admin.nested import NestedModelAdmin
from sortedm2m.fields import SortedManyToManyField

class Field(AbstractAccessInfoModel):

    FIELD_TYPES = (
        ("TEXT", "Text"),
        ("INTEGER", "Integer"),
        ("CHOICE", "Choice"),
        ("CHOICE+REMARK","Choice+Remark"),
        ("DROPDOWN", "Dropdown"),
    )


    field_name = models.CharField(max_length=512, blank=True)
    field_value = models.CharField(max_length=512,blank=True)
    description = models.CharField(max_length=512, blank=True)
    type = models.CharField(max_length=512, choices=FIELD_TYPES)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.field_name


class Form(AbstractAccessInfoModel):

    form_name = models.CharField(max_length=512, blank=True)
    description = models.CharField(max_length=512, blank=True)
    title = models.CharField(max_length=512, blank=True)
    category = models.CharField(max_length=512, blank=True)
    field = SortedManyToManyField(Field,blank=True)


    def __str__(self):
        return self.form_name


class Options(AbstractAccessInfoModel):
    OPTION_TYPES = (
        ("RADIO_BUTTON","Radio_button"),
        ("TEXT","Text"),
    )
    field = models.ForeignKey(Field, blank=False, null=False, on_delete=models.PROTECT)
    option_name = models.CharField(max_length=512, blank=True)
    option_type = models.CharField(max_length=512,choices=OPTION_TYPES,default='None')
    description = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return self.option_name

    class Meta:
        verbose_name_plural = "Options"


class Data(AbstractAccessInfoModel):
    choice = (
        ('ACCEPTED', 'Accepted'),
        ('REJECTED', 'Reject'),
        ('SEND_BACK', 'Send_Back'),

    )
    form = models.ForeignKey(Form, blank=False, null=False, on_delete=models.PROTECT)
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.PROTECT)
    form_data = models.JSONField(default=dict)
    status = models.CharField(max_length=512, choices=choice, default='Send_Back')
    form_remarks = models.TextField(max_length=1000, default='No Remarks')


    def __str__(self):
        return f"{self.form.form_name}  {self.user.first_name}"

    class Meta:
        verbose_name_plural = "All Form Data"

