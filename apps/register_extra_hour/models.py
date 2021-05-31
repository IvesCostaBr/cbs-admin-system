from django.db import models
from apps.collaborator.models import Collaborator
from django.db.models import signals
from django.dispatch import receiver
from django.utils import timezone



class RegisterExtraHour(models.Model):
    reason = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    collaborator = models.ForeignKey(Collaborator, on_delete=models.PROTECT)
    hours = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=30, default="Em Analise")

    def __str__(self):
        return str(self.reason)


@receiver(signals.post_save, sender=RegisterExtraHour)
def total_hours(sender, instance, **kwargs):
    Collaborator.objects.get(id=instance.collaborator.id).somar_horas()

@receiver(signals.post_delete, sender=RegisterExtraHour)
def delete_hours(sender, instance, **kwargs):
    Collaborator.objects.get(id=instance.collaborator.id).somar_horas()