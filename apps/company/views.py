from django.shortcuts import redirect, render, HttpResponse
from django.views.generic import CreateView
from django.views.generic.base import View
from django.views.generic.edit import UpdateView, DeleteView
#from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Company


class CreateCompany(CreateView):
    model = Company
    fields = ['name',]

    def form_valid(self, form):#TODO:Override no metodo from_valid a qual depois de salvar o obj no banco retorna o mesmo no metodo
        obj = form.save()
        self.request.user.collaborator.company = obj
        self.request.user.collaborator.save()
        return redirect('list_company')


class ListCompany(View):
    def get(self, request, *args, **kwargs):
        company_user = self.request.user.collaborator.company
        return render(request, 'company/company_list.html',{'company':company_user})
    
    
class UpdateCompany(UpdateView):
    model = Company
    fields = ('name',)


class DeleteCompany(DeleteView):
    model = Company
    





