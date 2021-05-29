from django.db import models
from apps.collaborator.models import Collaborator


class RegisterExtraHour(models.Model):
    reason = models.CharField(max_length=100)
    collaborator = models.ForeignKey(Collaborator, on_delete=models.PROTECT)
    hours = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.reason)