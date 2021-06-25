from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('admin', views.Admin.as_view(), name='admin'),
    path('new', views.Agent.new, name='new'),
    path('edit', views.Agent.edit, name='edit'),
    path('list', views.List.as_view(), name='user_list'),
]