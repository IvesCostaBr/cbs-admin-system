from django.db import models
from apps.company.models import Company
from django.urls import reverse



class Departament(models.Model):
    name_of_departament = models.CharField(max_length=80)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    #TODO:Caso de probelma no redirecionamento da url corrrigir o get absolute urls
    def get_absolute_url(self):
        return reverse('datail_departament',self.id)

    def __str__(self):
        return 'Name of Departament:'+ str(self.name_of_departament)
