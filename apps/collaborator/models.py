from django.db import models
from django.contrib.auth.models import User
from apps.departament.models import Departament
from apps.company.models import Company
from django.urls import reverse
from django.db.models import Sum



class CollaboratorManager(models.Model):
    def userOnline(self):
        return self.filter(logged=True)


class Collaborator(models.Model):


    STATUS_LOGGED = [
        (False, 'Offline'),
        (True, 'Online'),
    ]


    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    departaments = models.ManyToManyField(Departament, blank=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)
    total_horas = models.FloatField(default=00.00)
    profile_photo = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True, null=True)
    logged = models.BooleanField(default=False,choices=STATUS_LOGGED)


    objects = CollaboratorManager()


    class Meta:
        unique_together = [('user','cpf')]
    

    #TODO:set    
    def somar_horas(self):
        if  self.registerextrahour_set.filter(status=True).exists():
            total = self.registerextrahour_set.filter(
                status=True).aggregate(Sum('hours'))['hours__sum']
            collaborator = Collaborator.objects.get(id=self.id)
            collaborator.total_horas = total
            collaborator.save()
        else:
            collaborator = Collaborator.objects.get(id=self.id)
            collaborator.total_horas = 0.00
            collaborator.save()


    def get_absolute_url(self):
        return reverse('collaborator_page', args=[self.id])

    def __str__(self):
        return  str(self.user.first_name)




# @receiver(signals.pre_init, sender=Collaborator)
# def sendEmail(sender, **kwargs): 
#     print('print entrei no singal')
    
# @receiver(signals.pre_init, sender=Collaborator)
# def calculate_hour(sender, instance, **kwargs):
#     print('Sum')
#     return True




    