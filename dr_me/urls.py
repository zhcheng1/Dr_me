from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dr_me.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.default.urls')),
    url(r'^review-update/(?P<pk>[0-9]+)$', ReviewUpdate.as_view(), name='review-list'),
    url(r'^appointment/(?P<pk>[0-9]+)$', AppointmentUpdate.as_view(), name='appointment-list'),

)
