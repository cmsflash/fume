from typing import List, Union

from django.urls import re_path
from django.urls.resolvers import URLPattern, URLResolver

from . import views


urlpatterns: List[Union[URLPattern, URLResolver]] = [
    re_path(r'^(?P<game_id>[0-9]+)/add/$', views.add, name='add'),
]
