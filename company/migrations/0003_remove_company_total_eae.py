# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 14:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20170723_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='total_eae',
        ),
    ]
