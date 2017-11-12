# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 13:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(null=True)),
                ('detection', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.AddField(
            model_name='measurement',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Place'),
        ),
    ]
