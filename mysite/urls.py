"""mysite URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
import blog.views

urlpatterns = [
	url(r'^$', blog.views.index),
	url(r'^about/', blog.views.about),
	url(r'^ministries/', blog.views.ministries),
	url(r'^beliefs/', blog.views.beliefs),
	url(r'^sermon/', blog.views.sermon),
	url(r'^contact/', blog.views.contact),
	url(r'^events/', blog.views.events),
	url(r'^mission/', blog.views.mission),
	url(r'^fellowship/', blog.views.fellowship),
	url(
	    r'^blog/view/(?P<slug>[^\.]+).html', 
	    blog.views.view_post, 
	    name='view_blog_post'),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)