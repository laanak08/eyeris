from django.conf.urls import patterns, url#, include

from django.contrib import admin
admin.autodiscover()

from views import QueryPage

urlpatterns = patterns('',
#    url(r'^$', QueryPage.render_query_page),
    url(r'^$', QueryPage.render_query_page),
#    url(r'^test/', QueryPage.render_query_page ),
)
