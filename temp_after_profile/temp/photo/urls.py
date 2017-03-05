from django.conf.urls import patterns, include, url

urlpatterns = patterns('photo.views',
    url(r'^$', 'list', name='list'),
    url(r'^list/$', 'list', name='list'),
    url(r'^profile/$', 'profile', name='profile'),
    url(r'^main_profile/$', 'main_profile', name='main_profile'),
)