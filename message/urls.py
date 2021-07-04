# from app.message.form import Message
from django.urls import path, re_path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    #path('<type>', views.Message.as_view(), name=''),
    path('send', views.Message.send, name='send_message'),
    # url(r'^send/$', views.Message.send, name='send_message'),
    path('label/', views.Label.as_view(), name='label_list'),
    path('label/new', views.Label.new, name='label_new'),
    path('label/edit/<int:id>', views.Label.edit, name='label_edit'),
    path('label/delete/<int:id>', views.Label.delete, name='label_delete'),
    path('label/add/<str:chat_id>/<str:label>', views.Label.add, name='label_add'),
    path('agent/set_status/<str:chat_id>/<str:status>', views.Message.setStatus, name='set_status_message'),
    path('agent/set/<str:chat_id>/<str:status>/<str:agent_id>', views.Message.setAgent, name='set_agent_message')
]