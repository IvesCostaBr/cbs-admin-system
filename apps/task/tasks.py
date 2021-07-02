from celery import shared_task
from django.core.mail import send_mail
from apps.collaborator.models import Collaborator
from django.utils import timezone
from math import trunc

@shared_task
def send_relatorio():
    total = {}
    total = (Collaborator.objects.all().count())*8

    send_mail(
        f'[CBS-System] Relatorio Total de Colaboradores {timezone.now()}',
        f'Relatorio total de Funcionarios {trunc(total)}' ,
        'admin-sytem@cerberussistem.com.br ',
        ['ivescosta@cerberussistem.com.br'],
        fail_silently=False,
    )

