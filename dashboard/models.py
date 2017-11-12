# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return '{}'.format(self.name)


class Measurement(models.Model):
    value = models.IntegerField(null=True)
    detection = models.DateTimeField(auto_now=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return 'M_ID: {}'.format(self.id)
