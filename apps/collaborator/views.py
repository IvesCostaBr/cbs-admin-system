
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse
from django.views.generic import  ListView, DetailView, TemplateView
from django.views.generic.base import View
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from .models import Collaborator
from .forms import CollaboratorForm
from django.urls import reverse_lazy, reverse
from apps.departament.models import Departament
from apps.register_extra_hour.models import Point
from django.contrib.auth import views
from .reduce import createCollaborator



class LoginEnable(views.LoginView):
    def get_success_url(self):
        collaborator = Collaborator.objects.get(user=self.request.user)
        collaborator.logged = True
        collaborator.save()
        point = Point.objects.create(
            company=collaborator.company,
            collaborator=collaborator
            )
        print(point)
        point.save()
        return super(LoginEnable, self).get_success_url()


class LoginDisable(views.LogoutView):
    def dispatch(self, request, *args, **kwargs):
        collaborator = Collaborator.objects.get(user=self.request.user)
        collaborator.logged = False
        collaborator.save()
        return super(LoginDisable, self).dispatch(request,*args, **kwargs)

class CollaboratorPage(LoginRequiredMixin,DetailView):
    model = Collaborator
    template_name = 'collaborator/collaborator_page.html'

class HomeCollaboratorPainelAdmin(LoginRequiredMixin, TemplateView):
    template_name =  'collaborator/collaborator_painel_admin.html'

class CreateCollaborator(View):
    def get(self, request, *args, **kwargs):
        form = CollaboratorForm
        return render(self.request, 'collaborator/collaborator_form.html', {'form':form})

    def post(self, request, *args, **kwargs):
        form = CollaboratorForm(self.request.POST or None)
        if form.is_valid():
            createCollaborator(form, self.request)
            return redirect('painel_collaborator')
        return redirect('create_collaborator')


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
    fields = ('cpf','profile_photo')

    def get_absolute_url(self, *args, **kwargs):
        return reverse('collaobrator_page',)

class ListCollaborators(ListView):
    model = Collaborator
    
    def get_queryset(self):#TODO:Metodo faz override da queryset que o ListView injeta na pagina, dando assim liberdade de fazer o controle doque retornar ou mostrar
        company_logged = self.request.user.collaborator.company
        return Collaborator.objects.filter(company=company_logged)


class CollaboratorDelete(LoginRequiredMixin, DeleteView):
    model = Collaborator
    success_url = reverse_lazy('list_collaborators')

    def delete(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            if not self.object.user.is_staff:
                success_url = self.get_success_url()
                self.object.delete()
                return HttpResponseRedirect(success_url)
            else:
                return HttpResponse('Você não pode deletar um funcionario ADMIN.')
        except:
            return HttpResponse('Você não pode deletar esse usuario')


class CollaboratorDetail(LoginRequiredMixin, DetailView):
    model = Collaborator

def filtaFuncionario(request):
    depart = request.GET['other_params']
    departamento= Departament.objects.get(id=depart)
    qs_json = serializers.serialize('json', departamento.collaborato_set.all())
    return HttpResponse(qs_json, content_type='application/json')



def removeCollaborator(request, id):
    collaborator = Collaborator.objects.get(id=request.GET.get('id_collaborator'))

    if not collaborator.user.is_staff:
        collaborator.delete()
        return HttpResponse(collaborator)

