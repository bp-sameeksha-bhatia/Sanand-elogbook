# Generated by Django 3.1 on 2020-08-25 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elogbook', '0032_auto_20200825_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log_sheet_pcc',
            name='done_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 25, 19, 26, 11, 316435)),
        ),
    ]
