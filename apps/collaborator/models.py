from django.db import models
from django.contrib.auth.models import User
from apps.departament.models import Departament
from apps.company.models import Company

class Collaborator(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, unique=True)
    departaments = models.ManyToManyField(Departament)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return 'Collaborator Name:'+ str(self.first_name)