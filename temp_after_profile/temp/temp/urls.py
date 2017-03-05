
##from django.conf.urls import include, url
#from django.contrib import admin

##urlpatterns = [
 #   url(r'^admin/', include(admin.site.urls)),
#]

from django.conf.urls import patterns, include, url
from login.views import *

from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin
# admin.autodiscover

urlpatterns = patterns('',
                       url(r'^$', 'django.contrib.auth.views.login'),
                       url(r'^logout/$', logout_page),
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
                       # If user is not login it will redirect to login page
                       url(r'^register/$', register),
                       url(r'^register/success/$', register_success),
                       url(r'^home/$', home),
                       url(r'^profile/$',profile),
                       url(r'^photo/', include('photo.urls')),
                      url(r'^photo$', 'photo.views.list'),
                      url(r'^admin/', include(admin.site.urls)),
                      url(r'^home/photo$', 'photo.views.list'),
                      url(r'^home/profile$', 'photo.views.profile'),
                      url(r'^home/main_profile$', 'userprofile.views.user_profile'),
                      #url(r'^home_page/$','login.views.home')
                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



