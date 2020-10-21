# Generated by Django 3.1 on 2020-09-07 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocalendar', '0002_auto_20200902_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='form_remarks',
            field=models.TextField(default='No Remarks', max_length=1000),
        ),
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('ACCEPTED', 'Accepted'), ('REJECTED', 'Reject'), ('SEND_BACK', 'Send_Back')], default='Send_Back', max_length=512),
        ),
    ]