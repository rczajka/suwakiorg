from django.conf.urls import patterns, include, url


urlpatterns = patterns('suwaki.views',
    url(r'^$', 'home', name='home_page'),
    url(r'^get_news/$', 'news', name='suwaki_news'),
)
