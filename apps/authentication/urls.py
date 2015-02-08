from django.conf.urls import patterns, include, url

from rest_framework import routers

from views import *


# Can I simpily that?
router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = patterns(
     '',
    # ... URLs
    url((r'^auth/$'), include(router.urls)),
     url((r'^auth/login/$'), LoginView.as_view(), name='login'),
     url((r'^auth/logout/$'), LogoutView.as_view(), name='logout'),

)
