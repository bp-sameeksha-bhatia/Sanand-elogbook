# Generated by Django 3.1 on 2020-09-14 06:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elogbook', '0059_auto_20200914_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log_sheet_pcc',
            name='done_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 14, 11, 51, 42, 773533)),
        ),
    ]