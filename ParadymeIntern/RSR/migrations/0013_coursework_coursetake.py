# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-28 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RSR', '0012_person_workauthorization'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursework',
            name='Coursetake',
            field=models.ManyToManyField(through='RSR.PersonToCourse', to='RSR.Person'),
        ),
    ]