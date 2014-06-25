from django.conf.urls import patterns, include, url

from django.contrib import admin

from dict import views
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^word/(?P<word>\w+)/$', views.word),
)

