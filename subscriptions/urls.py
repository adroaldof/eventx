# coding: utf-8
from django.conf.urls import url, patterns


urlpatterns = patterns(
    'subscriptions.views',
    url(r'^$', 'subscribe', name='subscribe'),
    url(r'^(\d+)/$', 'detail', name='detail'),
)
