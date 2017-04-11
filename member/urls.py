from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .views import signup

urlpatterns = [
	url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'member/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'member/logout.html'}, name='logout'),
	url(r'^password_reset/$', auth_views.password_reset, {'template_name': 'member/password_reset.html', 'email_template_name': 'member/password_reset_email.html', 'post_reset_redirect': '/member/password_reset_done/'}, name='password_reset'),
	url(r'^password_reset_done/$', auth_views.password_reset_done, {'template_name': 'member/password_reset_done.html'},
		name='password_reset_done'),
	url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm, {'template_name': 'member/password_reset_confirm.html', 'post_reset_redirect': '/member/password_reset_complete/'}, name='password_reset_confirm'),
	url(r'^password_reset_complete/$', auth_views.password_reset_complete,
		{'template_name': 'member/password_reset_complete.html'}, name='password_reset_complete'),
]