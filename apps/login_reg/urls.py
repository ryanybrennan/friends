from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^main$', views.login_reg, name= 'login_reg'),
    url(r'^process/$', views.process, name = 'register'),
    url(r'^login/$', views.login, name = 'login'),
    url(r'^logoff$', views.logoff, name = 'logoff'),
]
