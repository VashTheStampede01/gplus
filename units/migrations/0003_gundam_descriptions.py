# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-15 01:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0002_auto_20190315_0123'),
    ]

    operations = [
        migrations.AddField(
            model_name='gundam',
            name='descriptions',
            field=models.TextField(blank=True, null=True),
        ),
    ]