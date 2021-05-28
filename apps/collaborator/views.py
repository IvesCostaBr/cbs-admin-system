from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.models import User
#from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Collaborator
from django.urls import reverse



class CollaboratorPage(DetailView):
    model = Collaborator
    template_name = 'collaborator/collaborator_page.html'

  


class HomeCollaboratorPainelAdmin(TemplateView):
    template_name =  'collaborator/collaborator_painel_admin.html'

class CreateCollaborator(CreateView):
    model = Collaborator
    fields = ('first_name','last_name', 'departaments', 'company')

    def form_valid(self, form):
        collaborator = form.save(commit=False)#TODO:Não manda para o banco apenas criar o objeto
        collaborator.company = self.request.user.collaborator.company
        username = collaborator.first_name + collaborator.last_name
        collaborator.user = User.objects.create(
            username=username)
        collaborator.save()
        return super(CreateCollaborator, self).form_valid(form)


class EditDataCollaborator(UpdateView):
    model= Collaborator
    fields = ('first_name','last_name', 'departaments')

    def get_absolute_url(self, *args, **kwargs):
        return reverse('home_page',)

class ListCollaborators(ListView):
    model = Collaborator
    
    def get_queryset(self):#TODO:Metodo faz override da queryset que o ListView injeta na pagina, dando assim liberdade de fazer o controle doque retornar ou mostrar
        company_logged = self.request.user.collaborator.company
        return Collaborator.objects.filter(company=company_logged)





class CollaboratorDelete(DeleteView):
    model = Collaborator

class CollaboratorDetail(DetailView):
    model = Collaborator
