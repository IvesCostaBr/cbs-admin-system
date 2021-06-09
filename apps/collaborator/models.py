from django.db import models
from django.contrib.auth.models import User
from apps.departament.models import Departament
from apps.company.models import Company
from django.urls import reverse
from django.db.models import Sum, F
from django.db.models import signals
from django.dispatch import receiver




class Collaborator(models.Model):

    STATUS_LOGGED = [
        (False, 'Offline'),
        (True, 'Online'),
    ]


    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    departaments = models.ManyToManyField(Departament, blank=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    total_horas = models.FloatField(default=00.00)
    profile_photo = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True, null=True)
    logged = models.BooleanField(default=False,choices=STATUS_LOGGED)

    class Meta:
        permissions = [
            ("gerente_geral", "ceo"),
        ]
    #TODO:Consertar a soma de horas     
    def somar_horas(self):
        if  self.registerextrahour_set.filter(status='Disponivel'):
            print(self.total_horas)
            total = self.registerextrahour_set.filter(status='Disponivel').aggregate(Sum('hours'))['hours__sum']
            Collaborator.objects.all().update(total_horas=total)
        else:
            Collaborator.objects.all().update(total_horas=0.00)
            

    def get_absolute_url(self):
        return reverse('collaborator_page', args=[self.id])

    def __str__(self):
        return  str(self.first_name) + '' + str(self.last_name)



@receiver(signals.post_save, sender=Collaborator)
def setar_total_horas(sender, instance, **kwargs):
    instance.somar_horas()
    