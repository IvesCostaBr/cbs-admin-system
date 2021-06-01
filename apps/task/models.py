from django.db import models
from apps.departament.models import Departament
from apps.collaborator.models import Collaborator
from django.utils import timezone

# Create your models here.

class Task(models.Model):

    STATUS_CHOICES = (
        (0, 'Não Concluido'),
        (1, 'Concluido'),
    )


    departament = models.ForeignKey(Departament, on_delete=models.PROTECT)
    collaborator = models.ForeignKey(Collaborator, on_delete=models.PROTECT)
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=300)
    date_creation = models.DateField(default=timezone.now)
    final_date = models.DateField(null=True, blank=True)
    status = models.BooleanField(choices=STATUS_CHOICES, default=0)


    def __str__(self):
        return str(self.id) + str(self.departament)+ str(self.title)

