# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-27 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djbugger', '0002_auto_20180516_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='exceptionshistory',
            name='exception_id',
            field=models.CharField(blank=True, max_length=2048, null=True, verbose_name='File Name'),
        ),
        migrations.AddField(
            model_name='exceptionshistory',
            name='status',
            field=models.CharField(blank=True, max_length=2048, null=True, verbose_name='File Name'),
        ),
    ]
