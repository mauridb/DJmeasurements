# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from be_rpi3.serializers import PlaceSerializer, MeasurementSerializer
from dashboard.models import Place, Measurement
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
# from django.http import HttpResponse
# from django.shortcuts import render

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


class PlaceViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    model = Place
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    # filter_fields = ('name',)


class MeasurementViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    model = Measurement
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    filter_fields = ('place', 'detection', 'value')
