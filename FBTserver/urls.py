from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FBTserver.views.home', name='home'),
    # url(r'^FBTserver/', include('FBTserver.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

)

urlpatterns += pattern('',
    url(r'^account/', inlcude('apps.account.urls'))
)

urlpatterns += pattern('',
    url(r'^admin/', include(admin.site.urls)),
)
