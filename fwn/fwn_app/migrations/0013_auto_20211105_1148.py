# Generated by Django 3.2.9 on 2021-11-05 18:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fwn_app', '0012_auto_20211105_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 5, 11, 48, 8, 272970)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 5, 11, 48, 8, 272970)),
        ),
    ]
