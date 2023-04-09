from typing import List, Union

from django.urls import re_path
from django.urls.resolvers import URLPattern, URLResolver

from . import views


urlpatterns: List[Union[URLPattern, URLResolver]] = [
    re_path(r'^(?P<game_product_id>[0-9]+)/$', views.purchase, name='purchase'),
    re_path(r'^(?P<game_product_id>[0-9]+)/pay/$', views.pay, name='pay'),
    re_path(r'^clear/(?P<game_id>[0-9]+)$', views.clear, name='clear'),
]
