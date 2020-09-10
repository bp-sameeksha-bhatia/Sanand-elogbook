from django.contrib import admin
from .models import *
from nested_admin.nested import NestedModelAdmin
from import_export.admin import ImportExportModelAdmin
from .resources import DataResource
from .views import export_json_field

class FormModelAdmin(admin.ModelAdmin):
    model = Form
    list_display = ['form_name', 'description', 'title', 'category']
    fields = ['form_name', 'description', 'title', 'category','field']
    list_per_page = 10


class FieldModelAdmin(admin.ModelAdmin):
    model = Field
    list_display = ['field_name', 'description', 'type', 'is_enabled']
    fields = ['field_name', 'description', 'type', 'is_enabled', 'options']
    list_per_page = 10


class OptionsModelAdmin(NestedModelAdmin):
    model = Options
    list_display = ['option_name', 'description']
    list_per_page = 10


class DataModelAdmin(ImportExportModelAdmin,NestedModelAdmin):
    model = Data
    list_display = ['event','form_data','created']
    readonly_fields = ['created','pk']
    resource_class = DataResource
    actions = [export_json_field,]

admin.site.register(Form, FormModelAdmin)
admin.site.register(Field, FieldModelAdmin)
admin.site.register(Options, OptionsModelAdmin)
admin.site.register(Data, DataModelAdmin)
