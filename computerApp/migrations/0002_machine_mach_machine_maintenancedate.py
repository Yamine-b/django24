# Generated by Django 4.0.3 on 2022-06-11 12:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='mach',
            field=models.CharField(choices=[('PC', 'PC - Run windows'), ('Mac', 'Mac - Run MacOS'), ('Serveur', 'Switch - To maintains and connect servers')], default='PC', max_length=32),
        ),
        migrations.AddField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 11, 12, 31, 36, 932712)),
        ),
    ]
