"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from blog.feed import LatestEntriesFeed
from blog import views as blog_views
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from blog.models import Entry

info_dict = {
    'queryset':Entry.objects.all(),
    'date_filed':'modified_time',

}

urlpatterns = [
    url(r'^$',blog_views.index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^comments/',include('django_comments.urls')),
    url(r'^latest/feed/$', LatestEntriesFeed()),
    url(r'^sitemap\.xml$',sitemap,{'sitemaps':{'blog':GenericSitemap(info_dict,priority=0.6)}},name='django.contrib.sitemaps.views.sitemap'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

handler403 = blog_views.permission_denied
handler404 = blog_views.page_not_found
handler500 = blog_views.page_error