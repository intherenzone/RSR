# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-09 23:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RSR', '0016_coursework_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursework',
            name='Course',
        ),
    ]