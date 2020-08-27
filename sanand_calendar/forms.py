from .models import Schedule
from django.forms import ModelForm
from django import forms


class CalendarForm(ModelForm):
    submit_by = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Schedule
        fields = '__all__'
