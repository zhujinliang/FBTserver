from django.conf.urls import patterns, include, url


urlpatterns = patterns('apps.account.views',
    url(r'^register/$', RegisterView.as_view()),
    url(r'^login/$', LoginView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
)
