from typing import List, Union

from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import re_path
from django.urls.resolvers import URLPattern, URLResolver

from . import views


urlpatterns: List[Union[URLPattern, URLResolver]] = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', views.index),
    re_path(r'^tags/', include(('tags.urls', 'tags'), namespace='tags')),
    re_path(r'^games/', include(('games.urls', 'games'), namespace='games')),
    re_path(r'^purchase/', include(
        ('purchase.urls', 'purchase'),namespace='purchase'
    )),
    re_path(r'^member/', include(('member.urls', 'member'), namespace='member')),
    re_path(r'^accounts/', include(('member.urls', 'member'), namespace='member')),
    re_path(r'^oauth/', include(
        ('social_django.urls', 'social'), namespace='social'
    )),
    re_path(r'^reviews/', include(
        ('reviews.urls', 'reviews'), namespace = 'reviews'
    )),
]

if settings.DEBUG is True:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
