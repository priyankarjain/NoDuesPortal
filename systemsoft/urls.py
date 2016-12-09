"""systemsoft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import  static
from django.conf import  settings
import nodues.views

app_name="nodues"

urlpatterns = [
    url(r'^$',nodues.views.hello,name="hello"),
    url(r'^admin/', admin.site.urls),
    url(r'^register/',include('registration.urls'),name="register"),
    url(r'^stud/$',nodues.views.loginHandler.as_view(),name="login"),
    url(r'^stud/login/$', nodues.views.stu),
    url(r'^stud/login/clearance$',nodues.views.sendClearence),
    url(r'^stud/logout/$', nodues.views.logout_view),
    url(r'^stud/login/genpdf$',nodues.views.formReceipt),
    #url(r'^stud/status$',nodues.views.statusView)
]
admin.site.site_header = 'NoDues administration'