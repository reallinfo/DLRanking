# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-13 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allframe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='frameinfo',
            name='sname',
            field=models.CharField(default=None, max_length=32),
        ),
    ]
