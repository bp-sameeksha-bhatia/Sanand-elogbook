# Generated by Django 3.1 on 2020-08-20 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanand_calendar', '0006_schedule_submit_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='submit_by',
            field=models.DateField(default=''),
        ),
    ]