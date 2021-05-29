from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.collaborator.models import Collaborator


#TODO:Assim que o USER entra ele não é um colcaborator verificar se ele é ou não antes de deixar ele cadastrar uma empresa
class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'core/home_page.html'
