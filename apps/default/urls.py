from django.conf.urls import patterns, include, url
from apps.default.views import *

urlpatterns = patterns(
    '',
    url(r'^doctors/$', DoctorList.as_view(), name='doctor-list'),
    url(r'^doctors/(?P<pk>[0-9]+)$', DoctorList.as_view(), name='doctor-list'),
    )
