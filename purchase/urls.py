from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<game_product_id>[0-9]+)/$', views.purchase),
]
