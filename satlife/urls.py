from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'satlife.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grammar/', include('grammar.urls')),
    url(r'^dict/', include('dict.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
