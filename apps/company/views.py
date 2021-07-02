from django.shortcuts import redirect, render, HttpResponse
from django.views.generic import CreateView
from django.views.generic.base import View
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Company
from django.urls import reverse_lazy
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType




class CreateCompany(LoginRequiredMixin, CreateView):
    model = Company
    fields = ['name', 'cnpj', 'telefone']
    def form_valid(self, form):
        obj = form.save(commit=False)
        if self.request.user.is_staff:
            obj.gerente = self.request.user
            obj.save()
        
        return redirect('redirect')


class ListCompany(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        self.request.session['company'] = 'cerberus'
        company_user = self.request.user.collaborator.company
        return render(request, 'company/company_list.html',{'company':company_user})
    
    
class UpdateCompany(LoginRequiredMixin, UpdateView):
    model = Company
    fields = ['name', 'cnpj', 'telefone']


class DeleteCompany(LoginRequiredMixin, DeleteView):
    model = Company
    success_url =  reverse_lazy('redirect')
    





