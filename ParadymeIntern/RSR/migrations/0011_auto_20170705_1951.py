# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-05 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RSR', '0010_auto_20170705_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='language',
            field=models.CharField(choices=[('English', 'English'), ('Spanish', 'Spanish'), ('French', 'French'), ('Chinese', 'Chinese')], max_length=30),
        ),
    ]