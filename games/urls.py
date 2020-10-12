from typing import List, Union

from django.conf.urls import url
from django.urls.resolvers import URLPattern, URLResolver

from .models import Game
from . import views


genres: str = '|'.join(
    [choice[1].lower() for choice in Game._meta.get_field('genre').choices]
)

urlpatterns: List[Union[URLPattern, URLResolver]] = [
    url(r'^(?P<gameID>[0-9]+)/$', views.game, name='game'),
    url(r'^(?P<gameID>[0-9]+)/tag$', views.tag, name='tag'),
    url(r'^(?P<gameID>[0-9]+)/tag/add$', views.add_tag, name='add_tag'),
    url(r'^genres/$', views.genres, name='genres'),
    url(r'^genres/(?P<genre>\w+)/$', views.genre, name='genre'),
    url(r'^purchased/$', views.purchased, name='purchased')
]
