# Generated by Django 3.1 on 2020-08-20 05:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elogbook', '0024_auto_20200820_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log_sheet_pcc',
            name='done_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 20, 10, 44, 44, 760185)),
        ),
    ]
