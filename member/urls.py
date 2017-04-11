from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .views import signup

urlpatterns = [
	url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'member/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'member/logout.html'}, name='logout'),
]