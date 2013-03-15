# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from .views import UrlList, IndexPage, UrlCreate, UrlRecoverRedirect, UrlAbout

urlpatterns = patterns('',
    url('^$',  IndexPage.as_view(), name='index'),
    url('^create/$', UrlCreate.as_view(), name='create'),
    url('^about/(?P<uri>[a-zA-Z0-9=\?]+)/$', UrlAbout.as_view(), name='about'),
    url('^list/$',UrlList.as_view(), name='list'),
    url('^(?P<uri>[a-zA-Z0-9=\?]+)/$', UrlRecoverRedirect.as_view(), name='redirecter'),
)