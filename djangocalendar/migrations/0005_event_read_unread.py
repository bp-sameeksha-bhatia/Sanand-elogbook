# Generated by Django 3.1 on 2020-09-08 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocalendar', '0004_auto_20200908_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='read_unread',
            field=models.BooleanField(default=False),
        ),
    ]