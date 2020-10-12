from typing import List, Union

from django.conf.urls import url
from django.urls.resolvers import URLPattern, URLResolver

from . import views


urlpatterns: List[Union[URLPattern, URLResolver]] = [
    url(r'^(?P<game_product_id>[0-9]+)/$', views.purchase, name='purchase'),
    url(r'^(?P<game_product_id>[0-9]+)/pay/$', views.pay, name='pay'),
    url(r'^clear/(?P<game_id>[0-9]+)$', views.clear, name='clear'),
]
