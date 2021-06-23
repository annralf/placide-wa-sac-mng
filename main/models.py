from django.db import models


class ActivitiesPerformance(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.CharField(max_length=45, blank=True, null=True)
    upated_at = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activities_performance'


class Client(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.CharField(max_length=45, blank=True, null=True)
    upated_at = models.DateField(blank=True, null=True)
    instance = models.TextField(blank=True, null=True)
    token = models.TextField(blank=True, null=True)
    api_setup = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client'


class ClientSession(models.Model):
    id = models.OneToOneField(Client, models.DO_NOTHING, db_column='id', primary_key=True)
    upated_at = models.DateField(blank=True, null=True)
    user = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_session'


class Labels(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.CharField(max_length=45, blank=True, null=True)
    upated_at = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'labels'


class LabelsClient(models.Model):
    label = models.ForeignKey(Labels, models.DO_NOTHING, blank=True, null=True)
    client = models.ForeignKey(Client, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'labels_client'


class Users(models.Model):
    id = models.OneToOneField(Client, models.DO_NOTHING, db_column='id', primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    lastname = models.CharField(max_length=45, blank=True, null=True)
    username = models.CharField(max_length=45, blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    role = models.ForeignKey('UsersRole', models.DO_NOTHING, db_column='role', blank=True, null=True)
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


class UsersRole(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.CharField(max_length=45, blank=True, null=True)
    upated_at = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_role'


class UsersStatus(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.CharField(max_length=45, blank=True, null=True)
    upated_at = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_status'
