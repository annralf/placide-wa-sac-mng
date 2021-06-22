from django import urls
from django.urls import re_path, path

from django.contrib import admin
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url('user/', include('user.urls')),
    url('message/', include('message.urls')),
    re_path(r'^$', views.Index.as_view(),name='index'),
    # re_path(r'^message/?', message.Message.as_view(),name='message'),
    re_path(r'^messages/?(?P<id>[\w@\.]+)?', views.messages, name='messages'),
    re_path(r'^agents/?(?P<name>[\w]+)?', views.agents, name='agents'),
    re_path(r'^chats/?', views.dialogs, name='dialogs'),
    re_path(r'^queue/?', views.queue, name='queue'),
    re_path(r'^hook/?$', views.hook, name='hook')
]