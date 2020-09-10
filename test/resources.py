from import_export import resources
from .models import Data
from import_export import fields, widgets

class DataResource(resources.ModelResource):
    data = fields.Field(widget=widgets.JSONWidget())
    class Meta:
        model = Data
        fields = ('event','form_data','created')
        exclude = ('created_by','modified_by')

