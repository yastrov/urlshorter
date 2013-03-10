# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from .views import create_url, recover_url, UrlList, IndexPage, about_url

urlpatterns = patterns('',
    url('^$',  IndexPage.as_view(), name='index'),
    url('^create/$', create_url, name='create'),
    url('^about/(?P<uri>.+)/$', about_url, name='about'),
    url('^list/$',UrlList.as_view(), name='list'),
    url('^(?P<uri>[a-zA-Z0-9=\?]+)/$', recover_url, name='redirecter'),
)
