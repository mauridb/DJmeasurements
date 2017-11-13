# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from dashboard.models import Place, Measurement
import time, random


def measurements(request):

    places = Place.objects.all()
    print places
    flag = 1
    while flag:
        # detected a measure
        for place in places:
            m = Measurement(value=random.randint(-30, 45), place=place)
            m.save()
            print "INFO: Great, measurement successfully detected .."
        time.sleep(1800) # 30 mins
