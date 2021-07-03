from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('admin', views.Admin.as_view(), name='admin'),
    path('new', views.Agent.new, name='new'),
    path('edit/<int:id>', views.Agent.edit, name='edit_user'),
    path('delete/<int:id>', views.Agent.delete, name='delete_user'),
    path('update/<int:id>', views.Agent.edit, name='update_user'),
    path('list/', views.List.as_view(), name='UserList'),
    path('rol/', views.Rol.as_view(), name='rol_list'),
    path('rol/new', views.Rol.new, name='rol_new'),
    path('rol/edit/<int:id>', views.Rol.edit, name='rol_edit'),
    path('rol/delete/<int:id>', views.Rol.delete, name='rol_delete'),
]