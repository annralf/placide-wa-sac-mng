from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    # path('<type>', views.Message.as_view(), name=''),
    url(r'^send/$', views.Message.send, name='send_message'),
    path('label/', views.Label.as_view(), name='label_list'),
    path('label/new', views.Label.new, name='label_new'),
    path('label/edit/<int:id>', views.Label.edit, name='label_edit'),
    path('label/delete/<int:id>', views.Label.delete, name='label_delete'),
]