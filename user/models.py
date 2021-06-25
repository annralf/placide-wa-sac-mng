from django.db import models
from client.models import Client, ActivitiesPerformance

class UsersRole(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.CharField(max_length=45, blank=True, null=True)
    upated_at = models.DateField(blank=True, null=True)
    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        managed = False
        db_table = 'users_role'

class Users(models.Model):
    id = models.OneToOneField(Client, models.DO_NOTHING, db_column='id', primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    lastname = models.CharField(max_length=45, blank=True, null=True)
    username = models.CharField(max_length=45, blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    role = models.ForeignKey( UsersRole,models.DO_NOTHING, db_column='role_id', blank=True, null=True )
    status = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)
    client_id = models.CharField(max_length=45, blank=True, null=True)

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
