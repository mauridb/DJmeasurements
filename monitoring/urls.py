"""monitoring URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from be_rpi3.views import PlaceViewSet, MeasurementViewSet

router_v1 = DefaultRouter()
router_v1.register(r'places', PlaceViewSet)
router_v1.register(r'measurements', MeasurementViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^measurements/', include('be_rpi3.urls')),
    url(r'^dashboard/', include('dashboard.urls')),

    # APIrest
    url(r'^api/v1/', include(router_v1.urls, namespace='api-root')),


]
