# Generated by Django 3.2.6 on 2021-08-18 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210818_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='creation_datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
