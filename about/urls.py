from django.conf.urls import patterns, include, url

from about import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ntmusic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^Actors/$',views.actors, name='actors'),
    url(r'^Nadezhda/$',views.chef,{'name':'Nadezhda'}, name='Nadezhda'),
    url(r'^Tatyana/$',views.chef,{'name':'Tatyana'}, name='Tatyana'),
    url(r'^$', views.hostess, name='Hostess'),

)
