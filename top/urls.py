from django.conf.urls import patterns, include, url

from top import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ntmusic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),

)
