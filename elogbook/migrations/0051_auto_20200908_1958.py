# Generated by Django 3.1 on 2020-09-08 14:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elogbook', '0050_auto_20200908_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log_sheet_pcc',
            name='done_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 8, 19, 58, 0, 846337)),
        ),
    ]
