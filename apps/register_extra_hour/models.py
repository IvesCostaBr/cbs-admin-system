from django.db import models
from apps.collaborator.models import Collaborator
from django.db.models import signals
from django.dispatch import receiver
from django.utils import timezone
from apps.company.models import Company



class RegisterExtraHour(models.Model):

    STATUS_HOURS = [
        (False, 'N/Disponivel'),
        (True, 'Disponivel')
    ]

    reason = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    collaborator = models.ForeignKey(Collaborator, on_delete=models.PROTECT)
    hours = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    status = models.BooleanField(default=False, choices=STATUS_HOURS)

    def __str__(self):
        return str(self.reason)


class PointManager(models.Manager):
    def exitPointRegister(self):
        p = self.last()
        p.date_logout = timezone.now()
        p.save()
        return True


class Point(models.Model):
    collaborator = models.ForeignKey(
        Collaborator, on_delete=models.PROTECT,
        blank=True, null=True
    )
    company = models.ForeignKey(
        Company, on_delete=models.PROTECT
    )
    date_login = models.DateTimeField(default=timezone.now)
    date_logout = models.DateTimeField(blank=True, null=True)
    horas_trabalhadas = models.FloatField(blank=True, null=True)

    objects = PointManager()

    def __str__(self):
        return str(self.collaborator)



@receiver(signals.post_save, sender=RegisterExtraHour)
def total_hours(sender, instance, **kwargs):
    Collaborator.objects.get(id=instance.collaborator.id).somar_horas()

@receiver(signals.post_delete, sender=RegisterExtraHour)
def delete_hours(sender, instance, **kwargs):
    Collaborator.objects.get(id=instance.collaborator.id).somar_horas()

