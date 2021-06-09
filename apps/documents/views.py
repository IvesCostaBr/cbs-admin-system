from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
    )
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
)
from .models import Document

class ListDocument(ListView):
    model = Document

    def get_queryset(self):
        if self.request.user.is_staff:
            return Document.objects.all()
        return Document.objects.filter(owner=self.request.user.collaborator)


class HomeDocument(TemplateView):
    template_name = 'documents/home_documents.html'

class CreateDocument(CreateView):
    model = Document
    fields = ['description','file']

    def form_valid(self, form):
        obj = form.save(commit=False)
        if self.request.user.is_staff:
            obj.save()
            return super(CreateDocument, self).form_valid(form)

        obj.owner = self.request.user.collaborator
        obj.save()
        return super(CreateDocument, self).form_valid(form)

    def get_success_url(self):
        return reverse('list_documents')

class UpdateDocument(UpdateView):
    model = Document
    fields = ['description','file']
    success_url =  reverse_lazy('list_documents')

class DeleteDocument(DeleteView):
    model = Document
    success_url =  reverse_lazy('list_documents')

class DetailDocument(DetailView):
    model = Document




