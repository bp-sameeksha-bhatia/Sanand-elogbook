# Generated by Django 3.1 on 2020-08-12 04:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elogbook', '0017_auto_20200811_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log_sheet_pcc',
            name='done_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 12, 10, 12, 42, 444165)),
        ),
    ]
