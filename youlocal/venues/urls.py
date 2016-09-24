from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'save_venue/$', views.saveVenue, name='saveVenue'),
    url(r'save_venue/rest/$', views.rest, name='rest')
]