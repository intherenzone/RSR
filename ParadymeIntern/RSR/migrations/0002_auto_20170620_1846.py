# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-20 18:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RSR', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='graduation_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='person',
            name='year_of_experience',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='person',
            name='awards',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='certificate',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='conference',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='skills',
            field=models.TextField(),
        ),
    ]