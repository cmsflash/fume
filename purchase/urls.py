from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<game_product_id>[0-9]+)/$', views.purchase, name='purchase'),
    url(r'^(?P<game_product_id>[0-9]+)/pay(?P<rewards_to_use>)', views.pay, name='pay'),
]
