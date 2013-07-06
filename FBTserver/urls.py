from django.conf.urls import patterns, include, url
from django.contrib import admin

from FBTserver.views import IndexView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='home'),
    # url(r'^FBTserver/', include('FBTserver.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

)

urlpatterns += patterns('',
    url(r'^account/', include('FBTserver.apps.account.urls')),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
