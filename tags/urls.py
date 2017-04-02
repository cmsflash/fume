from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<game_id>[0-9]+)/$', views.tag, name='tag'),
    url(r'^(?P<game_id>[0-9]+)/add/$', views.add, name='add'),
]
