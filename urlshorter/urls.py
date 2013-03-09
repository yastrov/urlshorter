from django.conf.urls import patterns, include, url
from settings import STATIC_ROOT, ROOT_PATH

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^(robots.txt)$', 'django.views.static.serve', {'document_root': STATIC_ROOT}),
    # Examples:
    # url(r'^$', 'urlshorter.views.home', name='home'),
    # url(r'^urlshorter/', include('urlshorter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'', include('shorter.urls')),
)
