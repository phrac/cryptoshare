from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'cryptoshare.views.index', name='index'),
    url(r'^about$', TemplateView.as_view(template_name="about.html")),
    url(r'^contact$', TemplateView.as_view(template_name="contact.html")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<base_62>.+)$', 'cryptoshare.views.viewmsg', name='encrypted'),

)
