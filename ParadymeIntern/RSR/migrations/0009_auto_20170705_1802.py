# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-05 18:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RSR', '0008_auto_20170705_1801'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='school_level',
            options={'ordering': ('school_level',)},
        ),
    ]