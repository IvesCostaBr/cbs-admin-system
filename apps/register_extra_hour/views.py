from django.shortcuts import render, HttpResponse
import json
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DetailView,
)
from django.views import View
from django.views.generic.edit import (
    DeleteView,
    UpdateView,
)
from .models import RegisterExtraHour
from django.urls import reverse_lazy
from .forms import HoraExtraForm
from django.forms.models import model_to_dict



class HomeHourDatabase(LoginRequiredMixin, TemplateView):
    template_name = 'register_extra_hour/painel_databasehour.html'

class CreateHourExtra(LoginRequiredMixin, CreateView):
    model = RegisterExtraHour
    form_class = HoraExtraForm
    success_url =  reverse_lazy('list_hour')

    def get_form_kwargs(self):#TODO:faz injeção de dados do form kwargs
        kwargs = super(CreateHourExtra, self).get_form_kwargs() #TODO:Carrega os kwargs os campos do form 
        kwargs.update({'user':self.request.user})
        return kwargs

class ListHourExtra(LoginRequiredMixin ,ListView):
    model = RegisterExtraHour
#TODO:Chave estrangeira sendo acessada através do campo collaborador    
    def get_queryset(self):
        return RegisterExtraHour.objects.filter(collaborator__company=self.request.user.collaborator.company)



class UpdateHourExtra(UpdateView):
    model = RegisterExtraHour
    fields = ('reason', 'hours', 'date', 'status')
    
    def get_success_url(self):
        return reverse_lazy('update_hour_extra', args=[self.object.id])

    

class DeleteHourExtra(DeleteView):
    model = RegisterExtraHour
    success_url =  reverse_lazy('list_hour')

class DetailHourExtra(DetailView):
    model = RegisterExtraHour


class UtilizarHoraExtra(View):
    def post(self, *args,**kwargs):
        hora = RegisterExtraHour.objects.get(id=kwargs['pk'])
        hora.status = "Ultilizada"
        hora.save()
        response = json.dumps({'mensagem':'Atualiado',
        'horas':float(hora.collaborator.total_horas)})
        return HttpResponse(response, content_type='application/json')


def disponibilizar_hora(request,id):
    hour = RegisterExtraHour.objects.get(id=id)
    hour.status = "Disponivel"
    hour.save()
    response = json.dumps({'mensagem':'Alteração Concluida', 
    'horas':float(hour.collaborator.total_horas)})
    return HttpResponse(response, content_type='application/json')