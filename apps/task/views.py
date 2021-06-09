from django.shortcuts import render, HttpResponse
from django.views.generic import (
    TemplateView,
    CreateView, 
    ListView,
    DetailView,
)
from django.views.generic.edit import UpdateView
from .models import Task
from django.urls import reverse_lazy
import xhtml2pdf.pisa as pisa
from django.template.loader import get_template
import io
from .tasks import send_relatorio
import json
from django.utils import timezone


class PainelTask(TemplateView):
    template_name = 'task/painel_task.html'


class CreateTask(CreateView):
    model = Task
    fields = (
        'departament',
        'collaborator',
        'title',
        'description',
        'date_creation',
        'final_date',
        'status')
    success_url = reverse_lazy('painel_task')


class ListTasks(ListView):
    model = Task

    def get_queryset(self):
        return Task.objects.filter(collaborator=self.request.user.collaborator)


class UpdateTask(UpdateView):
    model = Task
    fields = (
        'departament',
        'collaborator',
        'title',
        'description',
        'date_creation',
        'final_date',
        'status')
    success_url = reverse_lazy('painel_task')


class Render:
    @staticmethod
    def render(path:str, params:dict, filename:str):
        template = get_template(path)
        html =  template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")),response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' %filename
            return response
        else:
            return HttpResponse('Erro ao renderizar PDF',status=400)


def taskComplete(request, id):
    task = Task.objects.get(id=id)
    if task != None:
        task.status = 1
        task.final_date(timezone)
        task.save()
        response = json.dumps({ 'status':'Concluida'})
        return HttpResponse(response, content_type='application/json')



def relatorio_pdf(request):
    send_relatorio.delay()
    return HttpResponse('OK')



class DetailTask(DetailView):
    model = Task
    

# def disponibilizar_hora(request,id):
#     hour = RegisterExtraHour.objects.get(id=id)
#     hour.status = "Disponivel"
#     hour.save()
#     response = json.dumps({'mensagem':'Alteração Concluida', 
#     'horas':float(hour.collaborator.total_horas)})
#     return HttpResponse(response, content_type='application/json')