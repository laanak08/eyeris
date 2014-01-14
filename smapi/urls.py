from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from views import QueryPage

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'smapi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^test/', QueryPage.render_query_page ),
)
