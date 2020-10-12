from typing import List, Union

from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.urls.resolvers import URLPattern, URLResolver

from .views import signup


urlpatterns: List[Union[URLPattern, URLResolver]] = [
    url(r'^signup/$', signup, name='signup'),
    url(
        r'^login/$', auth_views.LoginView.as_view(),
        {'template_name': 'member/login.html'},
        name='login',
    ),
    url(
        r'^logout/$',
        auth_views.LogoutView.as_view(),
        {'template_name': 'member/logout.html'},
        name='logout',
    ),
    url(
        r'^password_reset/$',
        auth_views.PasswordResetView.as_view(),
        {
            'template_name': 'member/password_reset.html',
            'email_template_name': 'member/password_reset_email.html',
            'post_reset_redirect': '/member/password_reset_done/',
        },
        name='password_reset',
    ),
    url(
        r'^password_reset_done/$',
        auth_views.PasswordResetDoneView.as_view(),
        {'template_name': 'member/password_reset_done.html'},
	    name='password_reset_done',
    ),
    url(
        r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.PasswordResetConfirmView.as_view(),
        {
            'template_name': 'member/password_reset_confirm.html',
            'post_reset_redirect': '/member/password_reset_complete/',
        },
        name='password_reset_confirm',
    ),
    url(
        r'^password_reset_complete/$',
        auth_views.PasswordResetCompleteView.as_view(),
        {'template_name': 'member/password_reset_complete.html'},
        name='password_reset_complete',
    ),
]
