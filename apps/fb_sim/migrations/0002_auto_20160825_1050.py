# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 17:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fb_sim', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendship',
            name='friend',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friendfriend', to='login_reg.User'),
        ),
    ]
