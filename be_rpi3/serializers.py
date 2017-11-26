from rest_framework import serializers
from dashboard.models import Place, Measurement


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
        read_only_fields = ('id',)
        depth = 0


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'
        read_only_fields = ('id',)
        depth = 1
