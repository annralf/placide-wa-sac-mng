from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index,name='index'),
    re_path(r'^messages/?(?P<id>[\w@\.]+)?', views.messages, name='messages'),
    re_path(r'^agents/?(?P<name>[\w]+)?', views.agents, name='agents'),
    re_path(r'^chats/?', views.dialogs, name='dialogs'),
    re_path(r'^queue/?', views.queue, name='queue'),
    re_path(r'^hook/?$', views.hook, name='hook')
]
