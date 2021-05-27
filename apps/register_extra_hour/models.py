from django.db import models
from apps.collaborator.models import Collaborator


class RegisterExtraHour(models.Model):
    reason = models.CharField(max_length=100)
    collaborator = models.ForeignKey(Collaborator, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.reason)