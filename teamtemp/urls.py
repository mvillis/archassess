from django.conf.urls import patterns, include, url

from teamtemp.views import home, admin, submit

urlpatterns = patterns('',
    url(r'^$', home),
    url(r'^admin/([0-9a-z]{8})$', admin),
    url(r'^([0-9a-z]{8})$', submit),
)
