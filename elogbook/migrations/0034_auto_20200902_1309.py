# Generated by Django 3.1 on 2020-09-02 07:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elogbook', '0033_auto_20200825_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log_sheet_pcc',
            name='done_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 2, 13, 9, 12, 464745)),
        ),
    ]
