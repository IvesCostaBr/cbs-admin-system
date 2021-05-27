from django.db import models





class Departament(models.Model):
    name_of_departament = models.CharField(max_length=80)


    def __str__(self):
        return 'Name of Departament:'+ str(self.name_of_departament)
