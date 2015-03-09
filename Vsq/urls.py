from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
# import article

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Vsq.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^basicview/', include('article.urls')),
    url(r'^', include('article.urls')),
)
