# Generated by Django 3.1 on 2020-08-19 09:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elogbook', '0021_auto_20200819_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log_sheet_pcc',
            name='done_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 15, 21, 54, 222757)),
        ),
    ]