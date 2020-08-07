# Generated by Django 3.0.8 on 2020-08-07 07:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elogbook', '0011_auto_20200807_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chlorinated_soft_water_tank',
            name='done_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 7, 13, 26, 42, 356156)),
        ),
        migrations.AlterField(
            model_name='chlorinated_soft_water_tank',
            name='next_due_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 7, 13, 26, 42, 356156)),
        ),
        migrations.AlterField(
            model_name='chlorinated_soft_water_tank',
            name='title',
            field=models.CharField(default='Chlorinated_Soft_Water_Tank', max_length=800),
        ),
        migrations.AlterField(
            model_name='log_sheet_pcc',
            name='done_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 7, 13, 26, 42, 358157)),
        ),
    ]
