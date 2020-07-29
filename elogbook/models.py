from django.db import models
import datetime
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
        title = models.CharField(max_length=20,choices=(('1','Chlorinated_Soft_Water_Tank'),))
        doc_no = models.CharField(max_length=10)
        ref_sop_no = models.CharField(max_length=10)
        date = models.DateField(default=datetime.datetime.now())
        location = models.CharField(max_length=50)
        equipment_code = models.IntegerField()
        month = models.CharField(max_length=20,choices=month)
        frequency = models.CharField(max_length=20,choices =frequency)
        sr_no = models.IntegerField()
        activity = models.CharField(max_length=200,choices=activities)
        done_notdone = models.CharField(max_length=20,choices=ans)
        remarks = models.TextField(max_length=400)
        done_by = models.CharField(max_length=20)
        checked_by = models.CharField(max_length=40)
        done_on = models.DateTimeField(default=datetime.datetime.now())
        next_due_on = models.DateTimeField(default=datetime.datetime.now())

        def __str__(self):
            return self.title



