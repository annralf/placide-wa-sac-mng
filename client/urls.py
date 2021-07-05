from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',  views.Admin.as_view(), name='home'),
    path('new', views.New.as_view(), name='new-client'),
    path('edit/<int:id>', views.Admin.edit, name='edit'),
    path('delete/<int:id>', views.Admin.delete, name='delete_client'),
    path('show/<int:id>', views.Show.as_view(), name='show_client'),
    path('list', views.List.as_view(), name='admin'),
    # path('list', views.List.as_view(), name='list'),
]