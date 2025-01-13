from django.db import models

# Create your models here.
class AgentManagementNewAgentModel(models.Model):
    agent_id = models.BigIntegerField(null=True)
    name = models.CharField(max_length=300)
    phone = models.CharField(max_length=15)
    district = models.CharField(max_length=500, null=True)
    place = models.CharField(max_length=500, null=True)