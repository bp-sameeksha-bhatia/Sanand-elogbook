# Generated by Django 3.1 on 2020-09-03 13:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elogbook', '0045_auto_20200902_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log_sheet_pcc',
            name='done_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 3, 18, 58, 9, 694268)),
        ),
    ]
