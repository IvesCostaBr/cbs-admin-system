from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.models import User
#from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Collaborator
from .forms import CollaboratorForm
from django.urls import reverse_lazy, reverse
from apps.departament.models import Departament
from django.contrib.auth import views



class LoginEnable(views.LoginView):
    def get_success_url(self):
        collaborator = Collaborator.objects.get(user=self.request.user)
        collaborator.logged = True
        collaborator.save()
        return super(LoginEnable, self).get_success_url()


class LoginDisable(views.LogoutView):
    def dispatch(self, request, *args, **kwargs):
        collaborator = Collaborator.objects.get(user=self.request.user)
        collaborator.logged = False
        collaborator.save()
        return super(LoginDisable, self).dispatch(request,*args, **kwargs)

class CollaboratorPage(DetailView):
    model = Collaborator
    template_name = 'collaborator/collaborator_page.html'

class HomeCollaboratorPainelAdmin(TemplateView):
    template_name =  'collaborator/collaborator_painel_admin.html'

class CreateCollaborator(CreateView):
    template_name = 'collaborator/collaborator_form.html'
    form_class = CollaboratorForm


#TODO:realizar um refactore e from_valid
    def form_valid(self, form):
        collaborator = form.save(commit=False)#TODO:Não manda para o banco apenas criar o objeto  
        valid = Collaborator.objects.filter(user=self.request.user).exists()
        if valid == True:
            username = collaborator.first_name + collaborator.last_name
            collaborator.user = User.objects.create(
                username=username, password=username)
        else:
            collaborator.user = self.request.user
            
        collaborator.company = self.request.user.company_set.first()
        collaborator.save()  
        return super(CreateCollaborator, self).form_valid(form)




class EditDataCollaborator(UpdateView):
    model= Collaborator
    fields = ('first_name','last_name', 'departaments')

    def get_absolute_url(self, *args, **kwargs):
        return reverse('collaobrator_page',)

class ListCollaborators(ListView):
    model = Collaborator
    
    def get_queryset(self):#TODO:Metodo faz override da queryset que o ListView injeta na pagina, dando assim liberdade de fazer o controle doque retornar ou mostrar
        company_logged = self.request.user.collaborator.company
        return Collaborator.objects.filter(company=company_logged)


class CollaboratorDelete(DeleteView):
    model = Collaborator
    success_url = reverse_lazy('home_page')

class CollaboratorDetail(DetailView):
    model = Collaborator

def filtaFuncionario(request):
    from django.core import serializers
    from django.http import HttpResponse
    
    depart = request.GET['other_params']
    departamento= Departament.objects.get(id=depart)
    qs_json = serializers.serialize('json', departamento.collaborato_set.all())
    return HttpResponse(qs_json, content_type='application/json')