# Generated by Django 4.0.3 on 2022-05-18 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=200)),
            ],
        ),
    ]
