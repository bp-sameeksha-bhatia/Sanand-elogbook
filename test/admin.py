from django.contrib import admin
from .models import *
from nested_admin.nested import NestedModelAdmin


class FormModelAdmin(admin.ModelAdmin):
    model = Form
    list_display = ['form_name', 'description', 'title', 'category']
    fields = ['form_name', 'description', 'title', 'category','field']
    list_per_page = 10


class FieldModelAdmin(admin.ModelAdmin):
    model = Field
    list_display = ['field_name', 'description', 'type', 'is_enabled']
    list_per_page = 10


class OptionsModelAdmin(NestedModelAdmin):
    model = Options
    list_display = ['field', 'option_name', 'description']
    list_per_page = 10


class DataModelAdmin(NestedModelAdmin):
    model = Data
    list_display = ['form', 'user', 'form_data','created','status','form_remarks']
    readonly_fields = ['created','pk']


admin.site.register(Form, FormModelAdmin)
admin.site.register(Field, FieldModelAdmin)
admin.site.register(Options, OptionsModelAdmin)
admin.site.register(Data, DataModelAdmin)
