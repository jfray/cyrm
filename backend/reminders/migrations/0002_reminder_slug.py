# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminder',
            name='slug',
            field=models.SlugField(default='flurp', unique=True),
            preserve_default=False,
        ),
    ]
