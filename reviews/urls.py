from typing import List, Union

from django.conf.urls import url
from django.urls.resolvers import URLPattern, URLResolver

from . import views


urlpatterns: List[Union[URLPattern, URLResolver]] = [
    url(r'^(?P<game_id>[0-9]+)/add/$', views.add, name='add'),
]
