# Generated by Django 3.1 on 2020-08-24 11:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elogbook', '0030_auto_20200824_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log_sheet_pcc',
            name='done_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 24, 17, 10, 6, 654597)),
        ),
    ]
