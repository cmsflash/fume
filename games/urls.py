from typing import List, Union

from django.urls import re_path
from django.urls.resolvers import URLPattern, URLResolver

from .models import Game
from . import views


genres: str = '|'.join(
    [choice[1].lower() for choice in Game._meta.get_field('genre').choices]
)

urlpatterns: List[Union[URLPattern, URLResolver]] = [
    re_path(r'^(?P<gameID>[0-9]+)/$', views.game, name='game'),
    re_path(r'^(?P<gameID>[0-9]+)/tag$', views.tag, name='tag'),
    re_path(r'^(?P<gameID>[0-9]+)/tag/add$', views.add_tag, name='add_tag'),
    re_path(r'^genres/$', views.genres, name='genres'),
    re_path(r'^genres/(?P<genre>\w+)/$', views.genre, name='genre'),
    re_path(r'^purchased/$', views.purchased, name='purchased')
]
