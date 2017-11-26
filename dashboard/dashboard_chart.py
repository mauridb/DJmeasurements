from jchart import Chart

from dashboard.models import Measurement


class LineChart(Chart):
    chart_type = 'line'

    # Other option
    # responsive = False
    # layout =
    # title = "My dashboard chart"
    # legend =
    # tooltips =
    # hover =
    # animation =
    # elements =

    def get_datasets(self, *args, **kwargs):
        data = [{
            'label': "My dataset",
            'data': [m.value for m in Measurement.objects.all()],
        }]
        return data

    def get_labels(self, *args, **kwargs):
        return ["M_ID: {}".format(m.id) for m in Measurement.objects.all()]


class RadarChart(Chart):
    chart_type = 'radar'

    # Other option
    # responsive = False
    # layout =
    # title = "My dashboard chart"
    # legend =
    # tooltips =
    # hover =
    # animation =
    # elements =

    def get_datasets(self, *args, **kwargs):
        data = [{
            'label': "My dataset",
            'data': [m.value for m in Measurement.objects.all()],
        }]
        return data

    def get_labels(self, *args, **kwargs):
        return ["M_ID: {}".format(m.id) for m in Measurement.objects.all()]

