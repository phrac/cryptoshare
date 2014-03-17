from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'cryptoshare.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<base_62>.+)$', 'cryptoshare.views.viewmsg', name='encrypted'),

)
