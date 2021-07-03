from django.db import models
from django.utils import timezone

class Labels(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    status_label = models.IntegerField( db_column='status', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    upated_at = models.DateTimeField(auto_now_add=True)
    client_id =  models.IntegerField(blank=True, null=False)
    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        managed = False
        db_table = 'labels'