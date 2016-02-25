"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from test_app import views as test_app_views

urlpatterns = [
#	url(r'difAdd/(\d+)/(\d+)/$',test_app.old_add_redirect),
#	url(r'^new_add/(\d+)/(\d+)/$',test_app_views.difAdd,name='difAdd'),
#	url(r'^add/$',test_app_views.add,name='add'),
#	url(r'^$','test_app.views.index')
    url(r'^$','test_app.views.home',name='home'),
    url(r'^admin/',include(admin.site.urls)),
#    url(r'^admin/', admin.site.urls),
]
