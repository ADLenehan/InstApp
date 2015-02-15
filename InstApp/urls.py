from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'InstApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^hello/$', 'Moore.views.hello'),
    url(r'^hello_template/$', 'Moore.views.hello_template'),
    url('', include('social.apps.django_app.urls', namespace='social')),
)
