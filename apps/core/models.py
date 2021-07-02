from django.db import models
from django.utils import timezone
from apps.collaborator.models import Collaborator
from django.db.models import signals
from django.dispatch import receiver

class Notification(models.Model):

    MODULE_CHOICES = [
        (0, 'Modulo não declarado'),
        (1, 'Collaborator'),
        (2, 'Company'),
        (3, 'Departament'),
        (4, 'Documents'),
        (5, 'Hora Extra')
    ]

    date = models.DateTimeField(default=timezone.now)
    owner =  models.ForeignKey(Collaborator, on_delete=models.PROTECT, null=True, blank=True)
    titulo = models.CharField(max_length=40)
    modulo = models.IntegerField(default=0, choices=MODULE_CHOICES)
    description = models.CharField(max_length=300, blank=True, null=True)

