# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 16:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Place'),
        ),
    ]