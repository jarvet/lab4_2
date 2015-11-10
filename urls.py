"""hitzgwlab3 URL Configuration

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
from BookDB import views
#from django.contrib import admin

urlpatterns = [
#    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.main),
    url(r'^delete_book/(?P<ISBN>\d+)/$', views.delete_book),
    url(r'^add_book/$', views.add_book),
    url(r'^update_book/(?P<ISBN>\d+)/$', views.update_book),
    url(r'^add_author/$',views.add_author),
]
