"""desmondblog URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from blog import views
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.main_view),
    url(r'^home$', views.home_view, name="home"),
    url(r'^profile$', views.profile_view, name="profile"),
    url(r'^posts$', views.post_view, name="post"),
    url(r'^posts/new/$', views.post_view_new, name="post_new"),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.post_details_view, name="post_details"),
    url(r'^posts/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^posts/(?P<pk>[0-9]+)/edit/delete$', views.post_delete, name='post_delete'),
    url(r'^posts/(?P<pk>[0-9]+)/add_comment$', views.add_comment_to_post, name="add_comment_to_posts"),
    url(r'^posts/(?P<pk>[0-9]+)/flag_comment$', views.flag_comment, name="flag_comment"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
]
