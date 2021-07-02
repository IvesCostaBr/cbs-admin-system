# from celery import shared_task
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def sendEmailRegister(obj):
    subject = 'Bem Vindo ao HomeWork CBS.:)'
    html_message = render_to_string('email/new_collaborator.html', {'context': obj})
    plain_message = strip_tags(html_message)
    to = str(obj.user.email)

    mail.send_mail(subject,
    plain_message,
    'admin-sytem@cerberussistem.com.br',
    [to],
    html_message=html_message
    )
