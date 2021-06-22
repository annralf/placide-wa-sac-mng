from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('admin', views.Admin.as_view(), name='admin'),
    path('edit', views.Edit.as_view(), name='edit'),
    path('list', views.List.as_view(), name='list'),
]