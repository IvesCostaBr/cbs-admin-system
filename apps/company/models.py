from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import uuid




class Company(models.Model):
    name = models.CharField(max_length=100 ,help_text='Name of company')
    cnpj = models.CharField(max_length=15, null=True, blank=True)
    telefone = models.CharField(max_length=30, blank=True, null=True)
    cidade = models.CharField(max_length=30, blank=True, null=True)
    gerente = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    code_company = models.CharField(max_length=30, default=uuid.uuid4().hex[:6].upper())

    class Meta:
        unique_together = (['cnpj', 'code_company'])

    def get_absolute_url(self):
        return reverse('home_page_admin')

    def __str__(self):
        return 'Nome Empresa:' +  str(self.name)