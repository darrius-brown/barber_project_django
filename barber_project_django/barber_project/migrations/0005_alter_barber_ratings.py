# Generated by Django 4.1.1 on 2022-09-23 03:22

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barber_project', '0004_alter_barber_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barber',
            name='ratings',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None),
        ),
    ]
