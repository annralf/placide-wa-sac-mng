from django.db import models

class Cli(models.Model):

    @classmethod
    def getSetup(self, clientUser):
        return clientUser