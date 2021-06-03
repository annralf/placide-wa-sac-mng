#from djongo import models

#class Agent(models.Model):
#    agent_name = models.CharField(max_length = 20)
#    instances = models.JSONField(default = [])

#class Message(models.Model):
#    raw_data = models.JSONField()
#    ws_id = models.CharField(max_length = 50)
#    assigned = models.BooleanField(default = False)

#    class Meta:
#        abstract = True

#class Queue(models.Model):
#    message = models.EmbeddedField(
#        model_container = Message
#    )
