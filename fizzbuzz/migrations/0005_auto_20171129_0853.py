# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fizzbuzz', '0004_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='tests_passed',
            field=models.ManyToManyField(blank=True, default=None, to='fizzbuzz.Topic'),
        ),
    ]
