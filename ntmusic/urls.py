from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ntmusic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    #url(r'^article/', include('article.urls')),

    url(r'^afisha/', include('afisha.urls',namespace="afisha")),
    url(r'^about/',include('about.urls', namespace ="about")),
    url(r'^contacts/', include('contacts.urls',namespace="contact")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include ('top.urls', namespace="top")),


)
