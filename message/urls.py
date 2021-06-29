from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('<type>', views.Message.as_view(), name=''),
    url(r'^send/$', views.Message.send, name='send_message'),
]