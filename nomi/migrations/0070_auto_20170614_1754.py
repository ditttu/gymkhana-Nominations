# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomi', '0069_auto_20170614_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='room_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
