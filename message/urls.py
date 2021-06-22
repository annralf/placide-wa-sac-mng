from django.urls import path
from . import views

urlpatterns = [
    path('<type>', views.Message.as_view(), name='')
]