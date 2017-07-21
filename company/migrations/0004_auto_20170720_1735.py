# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-20 17:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20170720_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubsidiaryCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('estimated_annual_earnings', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.RenameModel(
            old_name='Company',
            new_name='MainCompany',
        ),
        migrations.AddField(
            model_name='subsidiarycompany',
            name='main_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.MainCompany'),
        ),
    ]
