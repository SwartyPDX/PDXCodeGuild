# Generated by Django 3.2.9 on 2021-11-05 00:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fwn_app', '0007_auto_20211104_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 4, 17, 50, 55, 665429)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 4, 17, 50, 55, 665429)),
        ),
    ]
