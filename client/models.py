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

class Cli(models.Model):

    @classmethod
    def getSetup(self, clientUser):
        current = Client.objects.get(name=clientUser)
        return { instance_id: current.instance, token: current.token }
