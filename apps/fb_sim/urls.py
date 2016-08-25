from django.conf.urls import url
from . import views
import re
urlpatterns = [
    url(r'^friends$', views.friends, name="homepage"),
    url(r'^user/(?P<id>\d+)$', views.profile, name= 'profile'),
    url(r'^add/(?P<id>\d+)$', views.add, name = 'add_friend'),
    url(r'^remove/(?P<id>\d+)$', views.remove, name = 'remove_friend'),
]
