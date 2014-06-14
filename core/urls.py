# coding: utf-8
from django.conf.urls import patterns, url


urlpatterns = patterns(
    'core.views',
    url(r'^$', 'home', name='home'),
    url(r'^palestrantes/$', 'speakers', name='speakers'),
    url(
        r'^palestrante/(?P<slug>[\w-]+)$',
        'speaker_detail',
        name='speaker_detail'
    ),
    url(r'^palestras/$', 'talk_list', name='talk_list'),
    url(r'^palestra/(?P<pk>\d+)/$', 'talk', name='talk'),
)
