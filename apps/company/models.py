from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100 ,help_text='Name of company')

    def __str__(self):
        return 'Nome Empresa:' +  str(self.name)