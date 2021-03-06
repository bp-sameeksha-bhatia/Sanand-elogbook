# Generated by Django 3.0.8 on 2020-07-31 03:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elogbook', '0004_auto_20200729_0846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chlorinated_soft_water_tank',
            name='doc_no',
        ),
        migrations.RemoveField(
            model_name='chlorinated_soft_water_tank',
            name='ref_sop_no',
        ),
        migrations.RemoveField(
            model_name='chlorinated_soft_water_tank',
            name='sr_no',
        ),
        migrations.AlterField(
            model_name='chlorinated_soft_water_tank',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 7, 31, 9, 27, 14, 131248)),
        ),
        migrations.AlterField(
            model_name='chlorinated_soft_water_tank',
            name='done_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 9, 27, 14, 131248)),
        ),
        migrations.AlterField(
            model_name='chlorinated_soft_water_tank',
            name='next_due_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 9, 27, 14, 131248)),
        ),
    ]
