from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import UploadFileForm, TaskForm
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


class PainelTask(LoginRequiredMixin, TemplateView):
    template_name = 'task/painel_task.html'


class CreateTask(LoginRequiredMixin, CreateView):
    template_name = 'task/task_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('painel_task')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.company = self.request.user.collaborator.company
        obj.save()
        return super(CreateTask, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(CreateTask, self).get_form_kwargs()
        kwargs.update({'company_obj':self.request.user.collaborator.company})
        return kwargs


class ListTasks(LoginRequiredMixin, ListView):
    paginate_by = 15
    model = Task

    def get_queryset(self):
        return Task.objects.filter(company=self.request.user.collaborator.company)


class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task/task_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('list_tasks')
    
    def get_form_kwargs(self):
        kwargs = super(UpdateTask, self).get_form_kwargs()
        kwargs.update({'company_obj':self.request.user.collaborator.company})
        return kwargs



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



class DetailTask(LoginRequiredMixin, DetailView):
    model = Task

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        form = UploadFileForm(self.request.POST or None, self.request.FILES or None)
        if form.is_valid():
            task.file_task = form.cleaned_data['file']
            task.save()
        return redirect(reverse('detail_task', args=[task.id]))

    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)
        context['form']= UploadFileForm()
        return context


def filtertask(request):
    if request.method == 'POST':
        value = request.POST['pesquisa']
        if Task.objects.filter(departament__name_of_departament=value).exists():
            query = Task.objects.filter(departament__name_of_departament=value)
        return render(request, 'task/filter_task.html',{'lista':query})
    return render(request, 'task/filter_task.html',{'lista':query})



#AJAX FUNCTIONS

def taskComplete(request, id):
    task = Task.objects.get(id=id)
    if task != None:
        if task.status == 0:
            task.status = 1
        else:
            task.status = 0
        task.final_date =  timezone.now()
        task.save()
        response = json.dumps({ 'status':'Concluida'})
        return HttpResponse(response, content_type='application/json')
    

def relatorio_pdf(request):
    send_relatorio.delay()
    return HttpResponse('OK')
