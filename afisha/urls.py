from django.conf.urls import patterns, include, url

from afisha import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ntmusic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^event/(?P<event_id>\d{1,4})/$', views.event, name='event'),
    url(r'^archives/$',views.archives, name='archives'),
    url(r'^all/$',views.all, name='all'),
    url(r'^$', views.coming, name='coming'),

)
