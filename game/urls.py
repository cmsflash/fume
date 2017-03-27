from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^(?P<game_id>\d+)$', views.viewGameDetails, name = 'view_game_details'),
]
