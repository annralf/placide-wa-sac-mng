from django.db import models
from django.utils import timezone
from client.models import Client, ActivitiesPerformance

class UsersRole(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    status_rol = models.IntegerField( db_column='status', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    upated_at = models.DateTimeField(auto_now_add=True)
    client_id =  models.IntegerField(blank=True, null=False)
    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        managed = False
        db_table = 'users_role'

class Users(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=45, blank=True, null=True)
    lastname = models.CharField(max_length=45, blank=True, null=True)
    username = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=False)
    role = models.ForeignKey(UsersRole,models.SET_NULL, db_column='role_id', blank=True, null=True )
    status_user = models.IntegerField( db_column='status', blank=True, null=True)
    created_at =models.DateTimeField(default=timezone.now)
    client_id =  models.IntegerField(blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'users'


class UsersActivityLog(models.Model):
    user = models.ForeignKey(Users, models.DO_NOTHING, db_column='user', blank=True, null=True)
    activity = models.ForeignKey(ActivitiesPerformance, models.DO_NOTHING, db_column='activity', blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_activity_log'


class UsersStatus(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.CharField(max_length=45, blank=True, null=True)
    upated_at = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_status'
