from django.db import models
from apps.departament.models import Departament
from apps.collaborator.models import Collaborator
from django.utils import timezone
from apps.company.models import Company




class Task(models.Model):

    STATUS_CHOICES = (
        (False, 'Não Concluido'),
        (True, 'Concluido'),
    )



    departament = models.ForeignKey(Departament, on_delete=models.PROTECT)
    collaborator = models.ForeignKey(Collaborator, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=300)
    date_creation = models.DateField(default=timezone.now)
    final_date = models.DateField(null=True, blank=True)
    file_task = models.FileField(upload_to='', blank=True, null=True)
    status = models.BooleanField(choices=STATUS_CHOICES, default=False)


    def __str__(self):
        return str(self.id) + str(self.departament)+ str(self.title)


class TaskApi(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    owner = models.ForeignKey(Collaborator, on_delete=models.PROTECT, null=True, blank=True)



