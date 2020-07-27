from .models import Electrical
from django.forms import ModelForm
from django import forms
class ChlorinatedForm(ModelForm):
    class Meta:
        model = Electrical.Chlorinated_Soft_Water_Tank
        fields = '__all__'


    widgets = {
        'date': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
        'done_on':forms.DateTimeInput(attrs={'class': 'datetime-input'}),
        'next_due_on':forms.DateTimeInput(attrs={'class': 'datetime-input'}),

    }



