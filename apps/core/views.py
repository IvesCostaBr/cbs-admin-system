from django.shortcuts import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View



#TODO:Assim que o USER entra ele não é um colcaborator verificar se ele é ou não antes de deixar ele cadastrar uma empresa
class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'core/home_page.html'



