from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^tags/', include('tags.urls', namespace='tags')),
    url(r'^games/', include('games.urls', namespace='games')),
    url(r'^purchase/', include('purchase.urls', namespace='purchase')),
    url(r'^member/', include('member.urls', namespace='member')),
    url(r'^accounts/', include('member.urls', namespace='member')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^reviews/', include('reviews.urls', namespace = 'reviews')),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
