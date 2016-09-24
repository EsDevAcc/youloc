from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls import url, include

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('venues.urls')),
    url(r'^venues/', include('venues.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

)

