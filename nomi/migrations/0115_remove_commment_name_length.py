# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-05 09:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nomi', '0114_auto_20170805_0915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commment',
            name='name_length',
        ),
    ]