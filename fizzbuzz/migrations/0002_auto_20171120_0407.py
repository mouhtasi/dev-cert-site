# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 04:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fizzbuzz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
