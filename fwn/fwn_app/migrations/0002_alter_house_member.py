# Generated by Django 3.2.7 on 2021-10-19 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fwn_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='house', to='fwn_app.member'),
        ),
    ]
