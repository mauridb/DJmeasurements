from django.conf.urls import url

from be_rpi3 import views

urlpatterns = [
    url(r'^$', views.measurements, name='measurements'),
]