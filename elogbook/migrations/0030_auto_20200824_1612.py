# Generated by Django 3.1 on 2020-08-24 10:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elogbook', '0029_auto_20200820_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log_sheet_pcc',
            name='done_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 24, 16, 12, 3, 665296)),
        ),
    ]