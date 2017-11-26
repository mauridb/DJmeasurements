# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from dashboard.models import Place, Measurement

admin.site.register(Place)
admin.site.register(Measurement)