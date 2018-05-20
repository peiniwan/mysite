"""mysite URL Configuration

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
from learn import views as learn_views  # new
from calc import views as calc_views
from people import views as people_views
from tools import views as tools_views
from meizi import views as meizi_views

urlpatterns = [
    url(r'^getlispic', meizi_views.getlispic, name='home'),
    url(r'^getlist', meizi_views.getlist, name='home'),
    # url(r'^', include('snippets.urls')),
    url(r'^$', tools_views.index, name='home'),
    url(r'^$', people_views.create, name='home'),
    url(r'^$', learn_views.home, name='home'),
    url(r'^$', calc_views.index, name='home'),
    url(r'^$', learn_views.index),  # new
    url(r'^admin/', admin.site.urls),
    url(r'^new_add/(\d+)/(\d+)/$', calc_views.add2, name='add2'),
    url(r'^add/$', calc_views.add, name='add'),
    url(r'^add/(\d+)/(\d+)/$', calc_views.add2, name='add2'),
]
