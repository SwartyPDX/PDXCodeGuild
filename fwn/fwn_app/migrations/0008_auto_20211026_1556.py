# Generated by Django 3.2.8 on 2021-10-26 22:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fwn_app', '0007_auto_20211022_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 26, 15, 56, 42, 433711)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 26, 15, 56, 42, 433711)),
        ),
    ]
