# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from dashboard.dashboard_chart import LineChart, RadarChart


def dashboard(request):
    context = {
        'line_chart': RadarChart(),
    }
    return render(request, 'dashboard.html', context)
