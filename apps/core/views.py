from django.shortcuts import HttpResponse, render, HttpResponseRedirect, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.urls import reverse
from django.contrib.auth.decorators import login_required


#TODO:Assim que o USER entra ele não é um colcaborator verificar se ele é ou não antes de deixar ele cadastrar uma empresa
class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'core/home_page_admin.html'

class Redirect(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            return redirect('home_page_admin')

        return redirect(reverse('collaborator_page', args=[self.request.user.collaborator.id]))

