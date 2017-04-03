from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'(\d+)(\+)(\d+)','calc.views.sum',),
    url(r'(\d+)(\*)(\d+)','calc.views.mul',),
    url(r'(\d+)(\/)(\d+)','calc.views.div',),
    url(r'(\d+)(-)(\d+)','calc.views.sub',),
    url(r'^admin/', include(admin.site.urls)),
)
