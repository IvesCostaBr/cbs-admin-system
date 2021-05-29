from django.db import models
from django.contrib.auth.models import User
from apps.departament.models import Departament
from apps.company.models import Company
from django.urls import reverse

class Collaborator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    departaments = models.ManyToManyField(Departament, blank=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('collaobrator_page', args=[self.id])

    def __str__(self):
        return 'Collaborator Name:'+ str(self.first_name)