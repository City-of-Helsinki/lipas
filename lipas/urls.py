from django.conf.urls import include, url
from django.contrib import admin

from venues.api import router

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'v1/', include(router.urls))
]
