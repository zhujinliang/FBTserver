from django.conf.urls import patterns, include, url
from FBTserver.apps.account.views import RegisterView
from FBTserver.apps.account.views import LoginView
from FBTserver.apps.account.views import LogoutView
from FBTserver.apps.account.views import SetPasswordView


urlpatterns = patterns('',
    url(r'^register/$', RegisterView.as_view()),
    url(r'^login/$', LoginView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^set-password/$', SetPasswordView.as_view()),
)
