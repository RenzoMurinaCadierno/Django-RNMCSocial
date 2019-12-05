"""simplesocial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^admin/',
        admin.site.urls),

    # render the HomePage view
    url(r'^$',
        views.HomePage.as_view(),
        name='home'),

    url(r'about/',
        views.AboutPage.as_view(),
        name='about'),

    # look for URLS in accounts.url, namespace 'accounts'
    #   > Namespace is to identify the group of urls altogether
    #   > This is to call them as template views {% accounts:index %}
    url(r'^accounts/',
        include('accounts.urls',
        namespace='accounts')),

    # and also connect everything under the module when accounts/
    # is called
    url(r'^accounts/',
        include('django.contrib.auth.urls')),

    url(r'^posts/',
        include('posts.urls', namespace='posts')),

    url(r'^groups/',
        include('groups.urls', namespace='groups')),
]
