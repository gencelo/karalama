from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from sitem.settings import MEDIA_ROOT, STATIC_ROOT

admin.autodiscover()
from blog.urls import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sitem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('blog.urls')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT }),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT }),
)


