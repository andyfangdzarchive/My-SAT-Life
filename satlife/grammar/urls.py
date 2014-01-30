from django.conf.urls import patterns, url

from grammar import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<grammar_id>\d+)/$', views.detail, name='detail'),
    url(r'^choose/$', views.choose, name='choose'),
    url(r'^list/$', views.list),
)