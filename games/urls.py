from django.conf.urls import url

from .models import Game
from . import views

genres = '|'.join([choice[1].lower() for choice in Game._meta.get_field('genre').choices])

urlpatterns = [
    url(r'^(?P<gameID>[0-9]+)/$', views.game, name='game'),
    url(r'^(?P<gameID>[0-9]+)/tag$', views.tag, name='tag'),
    url(r'^(?P<gameID>[0-9]+)/tag/add$', views.add_tag, name='add_tag'),
    url(r'^genres/$', views.genres),
    url(r'^genres/(?P<genre>[a-zA-Z]*" "*)/$', views.genre)
]
