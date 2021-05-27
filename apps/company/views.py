from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Company


class CreateCompany(CreateView):
    model = Company
    fields = ('name',)
    success_url = reverse_lazy('list_company')
   


class ListCompany(ListView):
    model = Company


class UpdateCompany(UpdateView):
    model = Company
    fields = ('name',)
  
    

class DeleteCompany(DeleteView):
    model = Company
    





