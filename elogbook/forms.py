from .models import Electrical
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django import forms
from django.utils.safestring import mark_safe
done = [
            ('Done','Done'),
            ('Not Done','Not Done'),
        ]
class ChlorinatedForm(forms.ModelForm):
    smbs = forms.ChoiceField(label='SMBS chemical dosing tank cleaning (T-965A)',choices=done,widget=forms.RadioSelect)
    smbs_dosing_pump = forms.ChoiceField(label='SMBS dosing pump, pipe, float switch, leakage from NRV to check. Attend, if any',choices=done,widget=forms.RadioSelect)
    chl_water_pump = forms.ChoiceField(label='Chlorinated water pump ( Motor connection tightening, earthing connections,motor pump guard, M-seal leakage, note motor ampere withdrawn',choices=done,widget=forms.RadioSelect)
    motor_bearing = forms.ChoiceField(label='Motor bearing and pump guard condition',choices=done,widget=forms.RadioSelect)
    water_leakage = forms.ChoiceField(label='Water leakage from M-seal or connected like connection. Attend if any',choices=done,widget=forms.RadioSelect)
    chlorine_sensor = forms.ChoiceField(label='Chlroine sensor housing leakage, membrane/electrolye replacement (when ever required',choices=done,widget=forms.RadioSelect)
    chl_sns_transmitter = forms.ChoiceField(label='Chlorine sensor transmitter calibration as per calibration plan',choices=done,widget=forms.RadioSelect)
    tank_top = forms.ChoiceField(label='Tank top ( dome) cleaning work',choices=done,widget=forms.RadioSelect)

    remark_smbs= forms.CharField(label='Remark', widget=forms.Textarea(attrs={'rows':1,'cols':22}))
    remark_dosing_pump = forms.CharField(label='Remark', widget=forms.Textarea(attrs={'rows':1,'cols':22}))
    remark_water_leakage= forms.CharField(label='Remark', widget=forms.Textarea(attrs={'rows':1,'cols':22}))
    remark_chlorine_sensor= forms.CharField(label='Remark', widget=forms.Textarea(attrs={'rows':1,'cols':22}))

    remark_motor_bearing= forms.CharField(label='Remark', widget=forms.Textarea(attrs={'rows':1,'cols':22}))
    remark_tank_top= forms.CharField(label='Remark', widget=forms.Textarea(attrs={'rows':1,'cols':22}))
    remark_chl_water_pump=forms.CharField(label='Remark', widget=forms.Textarea(attrs={'rows':1,'cols':22}))
    '''
    def __init__(self, *args, **kwargs):
        super(ChlorinatedForm, self).__init__(*args, **kwargs)
        for field in self.disabled_fields:
            self.fields[field].disabled = True

    
    #disabled_fields = ('done_by',)

    '''
    class Meta:
        model = Electrical.Chlorinated_Soft_Water_Tank
        fields = '__all__'
        exclude = ['date','done_on','next_due_on','status','location','month']






class Pcc(ModelForm):
    class Meta:
        model = Electrical.log_sheet_pcc
        fields = '__all__'




