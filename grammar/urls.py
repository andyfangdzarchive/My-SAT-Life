from django.conf.urls import patterns, url

from grammar import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^ajax/(?P<grammar_id>\d+)/$', views.detailJSON, name='detailJSON'),
    url(r'^ajaxD/(?P<grammar_id>\d+)/$', views.ajaxDetail, name='ajaxDetail'),
    url(r'^listajax/$', views.ajaxList),
    url(r'^view/(?P<grammar_id>\d+)/$', views.detail, name='detail'),
    url(r'^choose/(?P<pk>\d+)/$', views.choose, name='choose'),
    url(r'^list/$', views.list),
)