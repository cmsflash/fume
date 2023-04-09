from typing import List, Union

from django.urls import re_path
from django.urls.resolvers import URLPattern, URLResolver

from . import views


urlpatterns: List[Union[URLPattern, URLPattern]] = [
    re_path(r'^(?P<game_id>[0-9]+)/$', views.tag, name='tag'),
    re_path(r'^(?P<game_id>[0-9]+)/add/$', views.add, name='add'),
    re_path(
        r'^view/(?P<label>\w+.*)/$',
        views.view_games_by_tag,
        name='view_games_by_tag',
    ),
    re_path(r'^view_all_tags/$', views.view_all_tags, name='view_all_tags'),
]
