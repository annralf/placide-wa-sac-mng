from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^(?P<chat_id>[\w@\.]+)?', views.Admin.as_view(), name='admin'),
    path('new', views.New.as_view(), name='new-client'),
    path('edit', views.Edit.as_view(), name='edit'),
    path('list', views.List.as_view(), name='list'),
]