from django.contrib import admin
from user.models import Users, UsersRole, UsersStatus

admin.site.register(Users)
admin.site.register(UsersRole)
admin.site.register(UsersStatus)
