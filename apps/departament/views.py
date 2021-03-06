
from django.shortcuts import render
from django.views.generic.edit import (
    CreateView, 
    UpdateView, 
    DeleteView,
    )

from django.views.generic import (
    ListView,
    DetailView, 
    TemplateView
    )
from .models import Departament
from django.urls import reverse_lazy
from .forms import DepartamentsForm


class HomeDepartament(TemplateView):
    template_name = 'departament/home_departament.html'

class ListDepartament(ListView):
    model = Departament

    def get_queryset(self):
        return Departament.objects.filter(company=self.request.user.collaborator.company)

class CreateDepartament(CreateView):
    form_class = DepartamentsForm
    template_name = 'departament/departament_form.html'
    success_url =  reverse_lazy('list_departaments')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.company = self.request.user.collaborator.company
        obj.save()
        return super(CreateDepartament, self).form_valid(form)


class EditDepartament(UpdateView):
    form_class = DepartamentsForm
    template_name = 'departament/departament_form.html'
    success_url =  reverse_lazy('list_departaments')

class DeleteDepartament(DeleteView):
    model = Departament
    success_url =  reverse_lazy('list_departaments')

class DetailDepartament(DetailView):
    model = Departament


