# coding: utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(
        r'^inscricao/',
        include('subscriptions.urls', namespace='subscriptions')
    ),
    url(r'', include('core.urls', namespace='core')),
)
