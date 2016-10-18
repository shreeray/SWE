# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 14:15
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lawyered', '0002_auto_20161018_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='divorceForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spouse', models.CharField(max_length=25, verbose_name="What is your Spouse's name?")),
                ('date_of_marriage', models.DateField(default=datetime.date.today, verbose_name='What was your Date of Marriage?')),
                ('gender', models.CharField(max_length=1)),
                ('mutual', models.CharField(max_length=1)),
                ('assets', models.IntegerField()),
                ('assets_before', models.IntegerField()),
                ('children', models.CharField(max_length=1)),
                ('custody', models.CharField(max_length=1)),
                ('budget', models.CharField(max_length=250)),
                ('details', models.CharField(max_length=250)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
