from django.conf.urls import patterns, include, url
from blog.views import *

urlpatterns = patterns('',
    url(r'^$', "blog.views.makale_views", name="makale_views"),
    url(r'^(?P<slug>[-\w]+)/$', 'blog.views.makale_goster', name="makale_goster"),
    url(r'^(?P<slug>[-\w]+)/yorum_ekle/$', 'blog.views.yorum_ekle', name="yorum_goster"),
     )