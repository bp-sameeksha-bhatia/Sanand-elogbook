# Generated by Django 3.1 on 2020-09-08 14:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elogbook', '0051_auto_20200908_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log_sheet_pcc',
            name='done_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 8, 20, 1, 38, 172008)),
        ),
    ]