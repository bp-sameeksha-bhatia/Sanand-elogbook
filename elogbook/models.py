from django.db import models
import datetime
from django import forms
# Create your models here.
class Electrical(models.Model):

    class Chlorinated_Soft_Water_Tank(models.Model):
        activities = (
            ('1','SMBS chemical dosing tank cleaning (T-965A)'),
            ('2','SMBS dosing pump, pipe, float switch, leakage from NRV to check. Attend, if any'),
            ('3','Chlorinated water pump ( Motor connection tightening, earthing connections,motor pump guard, M-seal leakage, note motor ampere withdrawn'),
            ('4','Motor bearing and pump guard condition'),
            ('5','Water leakage from M-seal or connected like connection. Attend if any'),
            ('6','Chlorine sensor transmitter calibration as per calibration plan'),

            ('7','Chlroine sensor housing leakage, membrane/electrolye replacement (when ever required'),
            ('8','Tank top ( dome) cleaning work'),

        )
        ans = (
            ('1','Done'),
            ('2','Not Done'),
        )
        month = (
            ('1','January'),
            ('2', 'February'),
            ('3', 'March'),
            ('4', 'April'),
            ('5', 'May'),('6','June'),('7','July'),('8','August'),('9','September'),
            ('10', 'October'),('11','November'),('12','December'),


        )
        frequency = (
            ('1','Daily'),
            ('2','Weekly'),
            ('3','Monthly'),
            ('4','Quarterly'),
            ('5','Yearly'),

        )
        status = (
            ('1','PENDING'),
            ('2','ACCEPTED'),
            ('3','REJECTED'),
        )
        done = [
            ('Done','Done'),
            ('Not Done','Not Done'),
        ]
        title = models.CharField(default='Chlorinated_Soft_Water_Tank',max_length=800)
        #doc_no = models.CharField(max_length=10)
        #ref_sop_no = models.CharField(max_length=10)
        date = models.DateField(auto_now=True)
        location = models.CharField(max_length=50,default='Sanand,Gujarat')
        equipment_code = models.IntegerField()
        month = models.CharField(max_length=20,choices=month,default='January')
        frequency = models.CharField(max_length=200,default='Monthly')
        smbs = models.CharField(max_length=200)
        remark_smbs = models.CharField(max_length=50,default='No Remarks')
        smbs_dosing_pump = models.CharField(max_length=200)
        remark_dosing_pump = models.CharField(max_length=50, default='No Remarks')
        chl_water_pump = models.CharField(max_length=200)
        remark_chl_water_pump = models.CharField(max_length=50, default='No Remarks')
        motor_bearing = models.CharField(max_length=200)
        remark_motor_bearing = models.CharField(max_length=50, default='No Remarks')
        water_leakage = models.CharField(max_length=200)
        remark_water_leakage = models.CharField(max_length=50, default='No Remarks')
        chlorine_sensor = models.CharField(max_length=200)
        remark_chlorine_sensor = models.CharField(max_length=50, default='No Remarks')
        chl_sns_transmitter = models.CharField(max_length=200)
        remark_chl_sns_transmitter = models.CharField(max_length=50, default='No Remarks')
        tank_top = models.CharField(max_length=200)
        remark_tank_top = models.CharField(max_length=50, default='No Remarks')

        #sr_no = models.IntegerField()
        #activity = models.CharField(max_length=200,choices=activities)
        #done_notdone = models.CharField(max_length=20,choices=ans)
        #remarks = models.TextField(max_length=400)
        done_by = models.CharField(max_length=20)
        checked_by = models.CharField(max_length=40)
        done_on = models.DateTimeField(auto_now=True)
        next_due_on = models.DateTimeField(auto_now=True)
        status = models.CharField(max_length=50,choices=status,default='PENDING')

        def __str__(self):
            return self.title

    class log_sheet_pcc(models.Model):
        time_selection = (
            ('00', '00'),
            ('01', '01'),
            ('02', '02'),
            ('03', '03'),
            ('04', '04'),
            ('05', '05'),
            ('06', '06'),
            ('07', '07'),
            ('08', '08'),
            ('09', '09'),
            ('10', '10'),
            ('11', '11'),
            ('12', '12'),
            ('13', '13'),
            ('14', '14'),
            ('15', '15'),
            ('16', '16'),
            ('17', '17'),
            ('18', '18'),
            ('19', '19'),
            ('20', '20'),
            ('21', '21'),
            ('22', '22'),
            ('23', '23'),
        )

        shift_select = (('A', 'A'), ('B', 'B'), ('C', 'C'))

        icog_select = (('1', 'IC0G1'), ('2', 'IC0G2'))

        transformer_select = (('1', 'D-TR1'), ('2', 'D-TR2'))

        rtcc_select = (('1', 'RTCC1'), ('2', 'RTCC2'))

        apfc_select = (('1', 'APFC1'), ('2', 'APFC2'))

        power_control_select = (('1', 'Trafo-1'), ('2', 'Trafo-2'))

        done_on = models.DateTimeField(default=datetime.datetime.now())
        done_by = models.CharField(max_length=100)
        time_hr = models.CharField(choices=time_selection, max_length=20)
        shift = models.CharField(choices=shift_select, max_length=20)
        icog_ph_voltage_l1 = models.CharField(max_length=20)
        icog_ph_voltage_l2 = models.CharField(max_length=20)
        icog_ph_voltage_l3 = models.CharField(max_length=20)
        icog_ph_curr_r = models.CharField(max_length=20)
        icog_ph_curr_y = models.CharField(max_length=20)
        icog_ph_curr_b = models.CharField(max_length=20)
        icog_power_kwh = models.CharField(max_length=20)
        dist_transformer = models.CharField(choices=transformer_select, max_length=20)
        dt_winding_temp = models.CharField(max_length=20)
        dt_oil_temp = models.CharField(max_length=20)
        dt_oltc_counter = models.CharField(max_length=20)
        rtcc_panel = models.CharField(choices=rtcc_select, max_length=20)
        rtcc_tap_position = models.CharField(max_length=100)
        rtcc_winding_temp = models.CharField(max_length=20)
        rtcc_oil_temp = models.CharField(max_length=20)
        rtcc_volt_regulation_relay = models.CharField(max_length=20)
        apfc_panel = models.CharField(choices=apfc_select, max_length=20)
        apfc_power_factor = models.CharField(max_length=20)
        apfc_current = models.CharField(max_length=20)
        pcc_shift_operator = models.CharField(max_length=100)
        pcc = models.CharField(choices=power_control_select, max_length=20)
        pcc_volt_l1 = models.CharField(max_length=20)
        pcc_volt_l2 = models.CharField(max_length=20)
        pcc_volt_l3 = models.CharField(max_length=20)
        pcc_curr_r = models.CharField(max_length=20)
        pcc_curr_y = models.CharField(max_length=20)
        pcc_curr_b = models.CharField(max_length=20)
        pcc_power_kwh = models.CharField(max_length=20)
        remarks = models.CharField(max_length=500)

        def __str__(self):
            return self.done_on



