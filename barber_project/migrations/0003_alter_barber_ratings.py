# Generated by Django 4.1.1 on 2022-09-23 03:16

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barber_project', '0002_remove_barber_location_barber_city_barber_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barber',
            name='ratings',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None), size=None),
        ),
    ]
