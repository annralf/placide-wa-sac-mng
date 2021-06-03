from django.contrib import admin
from .models import Queue, Users, UsersRole, UsersStatus, Agent

admin.site.register(Users)
admin.site.register(UsersRole)
admin.site.register(Queue)
admin.site.register(UsersStatus)
admin.site.register(Agent)