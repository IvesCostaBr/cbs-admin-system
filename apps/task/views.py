from django.shortcuts import render, HttpResponse
from django.views.generic import (
    TemplateView,
    CreateView, 
    ListView,
)
from django.views.generic.edit import UpdateView
from .models import Task
from django.urls import reverse_lazy
import xhtml2pdf.pisa as pisa
from django.template.loader import get_template
import io
from .tasks import send_relatorio




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



def relatorio_pdf(request):
    send_relatorio.delay()
    return HttpResponse('OK')


