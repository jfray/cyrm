# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('publish_date', models.DateTimeField(verbose_name='date published')),
                ('run_date', models.DateTimeField(verbose_name='date to run')),
            ],
        ),
    ]
