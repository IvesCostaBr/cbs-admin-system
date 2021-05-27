from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView
from .models import Collaborator



class CreateCollaborator(CreateView):
    model = Collaborator
    fields = ('user','first_name','last_name', 'departaments', 'company')

def home(request):
    return HttpResponse('Ola')