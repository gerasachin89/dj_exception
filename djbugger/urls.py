from django.conf.urls import url, include
from django.contrib import admin
from . import views
from djbugger.views import ExceptionList, ExceptionDetail

urlpatterns = [
    url(r'^$', views.ExceptionList.as_view(),name='exception_list'),
    url(r'detail/(?P<pk>\d+)$', views.ExceptionDetail.as_view(),name='exception_detail'),

    url(r'list/$', views.success,name='exception_list'),
   ]
